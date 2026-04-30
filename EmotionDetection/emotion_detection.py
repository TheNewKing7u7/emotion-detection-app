"""
Módulo para la detección de emociones utilizando la API de Watson NLP.
Este módulo contiene la lógica para procesar texto y extraer puntajes emocionales.
"""
import json
import requests

def emotion_detector(text_to_analyze):
    """
    Analiza un texto dado y devuelve un diccionario con los puntajes de las emociones
    y la emoción dominante.
    """
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/' \
          'NlpService/EmotionPredict'
    header = {"GRP-Metadata": "watson.runtime.nlp.v1.models.ensemble.EmotionModel"}
    myobj = {"raw_document": {"text": text_to_analyze}}

    try:
        response = requests.post(url, json=myobj, headers=header, timeout=30)

        if response.status_code == 400:
            return {
                'anger': None, 'disgust': None, 'fear': None,
                'joy': None, 'sadness': None, 'dominant_emotion': None
            }

        formatted_response = json.loads(response.text)
        emotions = formatted_response['emotionPredictions'][0]['emotion']
        dominant_emotion = max(emotions, key=emotions.get)
        emotions['dominant_emotion'] = dominant_emotion

        return emotions

    except requests.exceptions.RequestException:
        return {
            'anger': None, 'disgust': None, 'fear': None,
            'joy': None, 'sadness': None, 'dominant_emotion': None
        }