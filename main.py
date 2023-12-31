from pytube import YouTube

#Çözünürlük için değiştir:
resolution = "480"

def Download(link):
    youtubeObject = YouTube(link)
    youtubeObject = youtubeObject.streams.filter(res=resolution).first()
    try:
        youtubeObject.download()
        print("Yükleme başarılı")
    except:
        print("Bir hata oluştu")


url = input("Enter the YouTube video URL: ")
Download(url)

