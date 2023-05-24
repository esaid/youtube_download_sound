import time
import pytube
# ecrire une fonction qui telecharge un video youtube et enregistre son nom dans un fichier
def download_video(url):
    yt = pytube.YouTube(url)
    video = yt.streams.first()
    video.download()
    return video.default_filename

# ecrire une fonction qui sauvegarde le son de la video youtube enregistré dans un fichier
def save_audio(filename):
    yt = pytube.YouTube(filename)
    audio = yt.streams.filter(only_audio=True).first()
    audio.download()
    return audio.default_filename

if __name__ == '__main__':
    url = input("Entrez l'url du video youtube : ")
    # filename = download_video(url)
    filename = save_audio(url)
    print("Le fichier a été téléchargé avec succès !")



