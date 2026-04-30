"""
Ejecución del servidor Flask para el sistema de detección de emociones.
Este módulo maneja las rutas de la interfaz web y la comunicación con
la lógica de procesamiento de emociones.
"""
from flask import Flask, render_template, request
from EmotionDetection.emotion_detection import emotion_detector

app = Flask("Emotion Detector")

@app.route("/emotionDetector")
def sent_analyzer():
    """
    Recibe el texto del usuario a través de una petición GET, lo procesa
    usando el detector de emociones y devuelve una respuesta formateada.
    """
    text_to_analyze = request.args.get('textToAnalyze')
    response = emotion_detector(text_to_analyze)

    # Validación de seguridad para entradas vacías o errores (Tarea 7)
    if response['dominant_emotion'] is None:
        return "¡Texto inválido! Por favor, intenta de nuevo."

    # Retorno del formato exacto solicitado en los lineamientos del proyecto
    return (
        f"Para la frase dada, la respuesta es: 'anger': {response['anger']}, "
        f"'disgust': {response['disgust']}, 'fear': {response['fear']}, "
        f"'joy': {response['joy']} y 'sadness': {response['sadness']}. "
        f"La emoción dominante es {response['dominant_emotion']}."
    )

@app.route("/")
def render_index_page():
    """
    Renderiza la página principal de la aplicación web.
    """
    return render_template('index.html')

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)