import requests
import os
import time

def get_image(url):
    response = requests.get(url, stream=True)
    if response.status_code == 200:
        filename = url.split('/')[-1]
        with open(filename, 'wb') as f:
            for chunk in response.iter_content(chunk_size=8192):
                f.write(chunk)
        return filename
    else:
        return None

def main():
    # Liste des URL des images à télécharger
    urls = [
        'https://genius.com/Don-krez-and-ronny-j-boomerang-annotated',
        'https://upload.wikimedia.org/wikipedia/commons/thumb/7/78/Van_Gogh_-_The_Starry_Night_-_Google_Art_Project.jpg/220px-Van_Gogh_-_The_Starry_Night_-_Google_Art_Project.jpg',
        'https://upload.wikimedia.org/wikipedia/commons/thumb/c/c1/The_Great_Wave_off_Kanagawa.jpg/220px-The_Great_Wave_off_Kanagawa.jpg'
    ]

    # Chemin du dossier de destination
    destination = 'grab'

    # Créer le dossier de destination si nécessaire
    if not os.path.exists(destination):
        os.makedirs(destination)

    # Télécharger les images
    for url in urls:
        filename = get_image(url)
        if filename is not None:
            print('Téléchargement de l\'image {} dans le dossier {}'.format(filename, destination))
            os.rename(filename, os.path.join(destination, filename))

if __name__ == '__main__':
    main()
