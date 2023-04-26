import qrcode
import os
import cv2
from PIL import Image,PngImagePlugin
import tkinter as tk
from tkinter  import *
from tkinter import filedialog
import PIL.Image


def mainPage():
    global page
    
    page = tk.Tk()
    page.title("Anasayfa")
    page.geometry("800x400")
    yazi= tk.Label(page, text="Yapmak İstediğiniz İşlemi Seçin",font=20,fg="BLACK")
    yazi.place(x=250,y=50)
    buton1=tk.Button(page, text="Görselleri Küçült", command=compressorWindow,font=20,height=2,)
    buton1.place(x=100, y=150)
    buton2 = tk.Button(page, text="Görselleri Boyutlandır",font=20,height=2,command=resize)
    buton2.place(x=300, y=150)
    buton3=tk.Button(page,text="QRCode Oluştur",font=20,height=2,command=createQrcode)
    buton3.place(x=550,y=150)
    buton4= tk.Button(page,text="PNG Dönüştür",font=20,height=2,command=convertPng)
    buton4.place(x=100,y=250)
    buton5= tk.Button(page, text="JPG Dönüştür",font=20,height=2,command=convertJpg)
    buton5.place(x=300,y=250)
    buton6=tk.Button(page, text="Webp Dönüştür",font=20,height=2,command=convertWebp)
    buton6.place(x=550, y=250)
    page.mainloop()
def compressorWindow():
    
    newPage= tk.Tk()
    
    newPage.geometry("800x400")
    page.destroy()
    
    inputPath= tk.Label(newPage,text="Görsellerin Bulunduğu Konumu Girin", font=5)
    inputPath.pack()
    entry1 = Entry(newPage, font=20)
    entry1.pack()
    outputPath=tk.Label(newPage,text="Görsellerin Kaydedileceği Konumu Girin", font=5)
    outputPath.pack()
    entry2 = Entry(newPage, font=20)
    entry2.pack()
    qualityPath=tk.Label(newPage,text="Görselin Kalitesi İçin 0-100 Arasında Değer Girin.", font=5)
    qualityPath.pack()
    qualityEntry=(Entry(newPage,font=20))
    qualityEntry.pack()

    label = Label(newPage)
    label.pack()
    errorLabel=tk.Label(newPage)
    errorLabel.pack()

    def compress_files():
        input1 = entry1.get()
        input2 = entry2.get()
        qualityInput= qualityEntry.get()
        
        count = 0
        
        for filename in os.listdir(input1):
                try:
                    with PIL.Image.open(os.path.join(input1, filename)) as im:
                        
                        im.save(os.path.join(input2, filename), optimize=True, quality=int(qualityInput))
                        count += 1
                except Exception as e:
                        errorLabel.config(text="Dosya Konumu, Türkçe Karakter, Görsel Dışı Format'a Dikkat Edin!",font=15)    
        label.config(text=str(count) + " Adet Resim Başarıyla Sıkıştırıldı!",font=15)
                

    button = Button(newPage, text="Dosyaları Sıkıştır", command=compress_files,font=20)
    button.pack()
     
    
    
    newPage.mainloop()
def resize():
    
    resizePage= tk.Tk()
    resizePage.title("Görselleri Boyutlandırma")
    resizePage.geometry("800x400")
    page.destroy()
    inputPathLabel=tk.Label(resizePage,text="Görsellerin Bulunduğu Konumu Girin",font=5)
    inputPathLabel.pack()
    inputPath=Entry(resizePage,font=20)
    inputPath.pack()
    outputPathLabel=tk.Label(resizePage,text="Görsellerin Kaydedileceği Konumu Girin", font=5)
    outputPathLabel.pack()
    outputPath=Entry(resizePage,font=20)
    outputPath.pack()
    widthLabel=tk.Label(resizePage,text="Genişlik Giriniz",font=10)
    widthLabel.pack()
    width=Entry(resizePage,font=20)
    width.pack()
    heightLabel=tk.Label(resizePage,text="Yükseklik Giriniz",font=10)
    heightLabel.pack()
    height =Entry(resizePage,font=20)
    height.pack()

    label = Label(resizePage)
    label.pack()
    errorMessage = Label(resizePage)
    errorMessage.pack()
    errorMessage2 = Label(resizePage)
    errorMessage2.pack()


    def resizeImage():
        widthInput = int(width.get())
        heightInput = int(height.get())
        imageInputPath = inputPath.get()
        imageOutputPath = outputPath.get()
        count = 0
        for filename in os.listdir(imageInputPath):
            
                try:
                    with PIL.Image.open(os.path.join(imageInputPath, filename)) as im:
                        newImage = im.resize((widthInput, heightInput))
                        newImage.save(os.path.join(imageOutputPath, filename))
                        count += 1
                except Exception as e:
                    errorMessage.config(text="Dosya Konumu, Türkçe Karakter, Görsel Dışı Format'a Dikkat Edin!", font=15)
                
        label.config(text=str(count) + " Adet Resim Başarıyla Boyutlandırıldı!", font=15)
    
    button = Button(resizePage, text="Resimleri Yeniden Boyutlandır", command=resizeImage,font=20)
    button.pack()
    resizePage.mainloop()
def createQrcode():
    qrPage=tk.Tk()
    qrPage.geometry("800x400")
    qrPage.title("Qr Oluşturma Sayfası")
    page.destroy()
    inputLabel=tk.Label(qrPage,text="QRcode Oluşturmak İstediğiniz Linki Girin",font=5)
    inputLabel.pack()
    inputEntry=Entry(qrPage,font=20)
    inputEntry.pack()
    nameLabel=tk.Label(qrPage,text="Oluşturulacak QRCode İsmini Girin",font=5)
    nameLabel.pack()
    nameEntry=Entry(qrPage,font=20)
    nameEntry.pack()
    saveInputLabel=tk.Label(qrPage,text="QRcode Görselini Kayıt Etmek İstediğiniz Dosyayı Belirtin",font=5)
    saveInputLabel.pack()
    saveInputEntry=Entry(qrPage,font=20)
    saveInputEntry.pack()
    
    label=tk.Label(qrPage)
    label.pack()
    def qr():
        link=inputEntry.get()
        output=saveInputEntry.get()
        name=nameEntry.get()
        try:
            newQr=qrcode.make(link)
            newQr.save(os.path.join(output,name+".png"))
            label.config(text="QrCode Başarıyla Oluşturuldu.",font=15)
        except Exception as e:
                    label.config(text="Dosya Konumu, Türkçe Karakter, Görsel Dışı Format'a Dikkat Edin!", font=15)
    buton=tk.Button(qrPage,text="QRcode Oluştur",font=20,command=qr)
    buton.pack()
    

    qrPage.mainloop()
def convertWebp():
    webpPage=tk.Tk()
    webpPage.geometry("800x400")
    webpPage.title("Webp Dönüştürme")
    page.destroy()
    inputPathLabel=tk.Label(webpPage,text="Görsellerin Bulunduğu Konumu Girin",font=5)
    inputPathLabel.pack()
    inputPath=Entry(webpPage,font=20)
    inputPath.pack()
    outputPathLabel=tk.Label(webpPage,text="Görsellerin Kaydedileceği Konumu Girin", font=5)
    outputPathLabel.pack()
    outputPath=Entry(webpPage,font=20)
    outputPath.pack()
    message= tk.Label(webpPage)
    message.pack()

    def Webp():
        imageInputPath = inputPath.get()
        imageOutputPath= outputPath.get()
        count=0
        for fileName in os.listdir(imageInputPath):
            try:
                with PIL.Image.open(os.path.join(imageInputPath,fileName)) as im:
                    name, extension= os.path.splitext(fileName)
                    newImage= name+".webp"
                    newImagePath= os.path.join(imageOutputPath,newImage)
                    im.save(newImagePath,"WEBP")                
                    count+=1

            except Exception as e:
                    message.config(text="Dosya Konumu, Türkçe Karakter, Görsel Dışı Format'a Dikkat Edin!", font=15)
        message.config(text=str(count)+" Adet Resim Dönüştürüldü!",font=15)
    button = Button(webpPage, text="Resimleri Dönüştür", command=Webp,font=20)
    button.pack()      
    webpPage.mainloop()
def convertJpg():
    jpgPage=tk.Tk()
    jpgPage.geometry("800x400")
    jpgPage.title("Jpg Dönüştürme")
    page.destroy()
    inputPathLabel=tk.Label(jpgPage,text="Görsellerin Bulunduğu Konumu Girin",font=5)
    inputPathLabel.pack()
    inputPath=Entry(jpgPage,font=20)
    inputPath.pack()
    outputPathLabel=tk.Label(jpgPage,text="Görsellerin Kaydedileceği Konumu Girin", font=5)
    outputPathLabel.pack()
    outputPath=Entry(jpgPage,font=20)
    outputPath.pack()
    message= tk.Label(jpgPage)
    message.pack()

    def Jpg():
        imageInputPath = inputPath.get()
        imageOutputPath= outputPath.get()
        count=0
        for fileName in os.listdir(imageInputPath):
            try:
                with PIL.Image.open(os.path.join(imageInputPath,fileName)) as im:
                    name, extension= os.path.splitext(fileName)
                    newImage= name+".jpg"
                    newImagePath= os.path.join(imageOutputPath,newImage)
                    im.save(newImagePath,"JPEG")                
                    count+=1

            except Exception as e:
                message.config(text="Dosya Konumu, Türkçe Karakter, Görsel Dışı Format'a Dikkat Edin!", font=15)
        message.config(text=str(count)+" Adet Resim Dönüştürüldü!",font=15)
    button = Button(jpgPage, text="Resimleri Dönüştür", command=Jpg,font=20)
    button.pack()      
    jpgPage.mainloop()
def convertPng():
    pngPage=tk.Tk()
    pngPage.geometry("800x400")
    pngPage.title("Png Dönüştürme")
    page.destroy()
    inputPathLabel=tk.Label(pngPage,text="Görsellerin Bulunduğu Konumu Girin",font=5)
    inputPathLabel.pack()
    inputPath=Entry(pngPage,font=20)
    inputPath.pack()
    outputPathLabel=tk.Label(pngPage,text="Görsellerin Kaydedileceği Konumu Girin", font=5)
    outputPathLabel.pack()
    outputPath=Entry(pngPage,font=20)
    outputPath.pack()
    message= tk.Label(pngPage)
    message.pack()
    def Png():
        imageInputPath = inputPath.get()
        imageOutputPath= outputPath.get()
        count=0
        for fileName in os.listdir(imageInputPath):
            try:
                with PIL.Image.open(os.path.join(imageInputPath,fileName)) as im:
                    name, extension= os.path.splitext(fileName)
                    newImage= name+".png"
                    newImagePath= os.path.join(imageOutputPath,newImage)
                    im.save(newImagePath,"PNG")                
                    count+=1

            except Exception as e:
                message.config(text="Dosya Konumu, Türkçe Karakter, Görsel Dışı Format'a Dikkat Edin!", font=15)
        message.config(text=str(count)+" Adet Resim Dönüştürüldü!",font=15)
    button = Button(pngPage, text="Resimleri Dönüştür", command=Png,font=20)
    button.pack()
    pngPage.mainloop()
mainPage()  


