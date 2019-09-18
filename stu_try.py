import os
import imageio
import time
from PIL import Image, ImageDraw
import shutil
import random

SOURCE_PATH = 'C:/Work/Python/ASCII Art'+'./1.gif'  # 源图片路径
OUTPUT_PATH = 'C:/Work/Python/ASCII Art/out/'  # 解析路径 存放每一帧的图片
FRAMES_PATH = 'C:/Work/Python/ASCII Art/frame/'  # 转字符路径 存放转化为字符画的每一帧图片

    

def create_dir():
	if (os.path.exists(OUTPUT_PATH)):
		print("Yes!")
	else:
		print("Creating...")
		os.makedirs(OUTPUT_PATH)
		os.makedirs(FRAMES_PATH)
		time.sleep(3)
		print("Finished!")

def processImage(path):
    # 提取每一帧的图片，这里用捕获异常的方式遍历整个gif
	img = Image.open(path)
	index = 0 
	print('正在解析.....')
	try:
		while True:
			img.seek(index)
			img.save(os.path.abspath('C:/Work/Python/ASCII Art/out/%d.png' % index))
			index += 1
	except EOFError:
		print("共截取%d张!" % index)
		print('解析完成！')


def createImg(path):
	print("START")
	CHARACTER = "@.B08&WM#*oahkbdpqwmZO0QLCJUYXzcvunxrjft/()1[]?-_+~<>i!lI;:,."
	count = len(CHARACTER)
	for file in os.listdir(path):
		with Image.open(''.join((path, file))) as img:
			width, height =img.size
			img = img.convert("RGB")
			#print(width,height)
			new_img = Image.new('1', (width*2, height*2), color=255)
			draw = ImageDraw.Draw(new_img)
			for heightp in range(1,height,4):  
				for widthp in range(1,width,4):
					R,G,B = img.getpixel((widthp,heightp)) 
					#print(R,G,B)
					gray = int(R* 0.299+G* 0.587+B* 0.114)
					conf = int(gray/count)
					if conf != 4:
						draw.text((widthp*2,heightp*2),CHARACTER[conf])
			new_img.save('C:/Work/Python/ASCII Art/frame/'+ file)
	print("END!")
    

def create_gif(path, filename):
	print('正在生成GIF.....')
	image_list = []
	num = len(os.listdir(path))
	for i in range(num):
		image_list.append('C:/Work/Python/ASCII Art/frame/' + str(i) + '.png')
	frames = []
	for image_name in image_list:
		frames.append(imageio.imread(image_name))
   # Save them as frames into a gif
	imageio.mimsave(filename, frames, 'GIF', duration=0.1)
	print('已生成GIF！')


def main():
	create_dir()
	processImage(SOURCE_PATH)
	createImg(OUTPUT_PATH)
	create_gif(FRAMES_PATH, '001.gif')
	val = random.randint(0,9999999999)
	shutil.rmtree("C:/Work/Python/ASCII Art/out")
	shutil.rmtree("C:/Work/Python/ASCII Art/frame")
	shutil.move("C:/Work/Python/ASCII Art/1.gif", "C:/Work/Python/ASCII Art/finished_raw/%d.gif"%val)
	shutil.move("C:/Work/Python/ASCII Art/001.gif","C:/Work/Python/ASCII Art/finished_prod/%d.gif"%val)

if __name__ == '__main__':
	main()
