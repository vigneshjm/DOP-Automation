from google.cloud import vision
import os
import io

credential_path = "\\Users\\HP\\Downloads\\dopautom-9f2f1a082393.json"
os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = credential_path

def detect_text(path):
    """Detects text in the file."""
    client = vision.ImageAnnotatorClient()

    with io.open(path, 'rb') as image_file:
        content = image_file.read()

    image = vision.Image(content=content)

    response = client.text_detection(image=image)
    texts = response.text_annotations
    print('Texts:{}'.format(texts[0].description))

    if response.error.message:
        raise Exception(
            '{}\nFor more info on error messages, check: '
            'https://cloud.google.com/apis/design/errors'.format(
                response.error.message))

detect_text('\\Users\\HP\\Desktop\\Git Repo\\DOP Automation\\Cropped Image.jpg')