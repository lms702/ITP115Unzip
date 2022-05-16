import os
import time
from zipfile import ZipFile
from subprocess import run

DOWNLOADS_FOLDER = 'C:/Users/Scottie/Downloads'
try:
	os.mkdir(f'{DOWNLOADS_FOLDER}/ITPUnzip')
except FileExistsError:
	print('ITPUnzip folder already exists!')
else:
	print('ITPUnzip folder created!')

UNZIP_FOLDER = f'{DOWNLOADS_FOLDER}/ITPUnzip'

initialDownloads = set(os.listdir(DOWNLOADS_FOLDER))
numDownloads = len(initialDownloads)
# keep checking downloads folder to see if there are any new files
while True:
	# input("new file?")
	time.sleep(1)
	downloads = os.listdir(DOWNLOADS_FOLDER)
	if len(downloads) != numDownloads:
		time.sleep(2)  # to ignore temporary files associated with downloads
		downloads = os.listdir(DOWNLOADS_FOLDER)
		if len(downloads) != numDownloads:
			# new download
			downloads = set(downloads)
			newFile = list(downloads.difference(initialDownloads))[0]
			print(f'\n\nDetected new file: {newFile}')

			# move file from downloads to ITPUnzip folder
			os.rename(f'{DOWNLOADS_FOLDER}/{newFile}', f'{UNZIP_FOLDER}/{newFile}')
			
			# see if it is a zip or a py or something else
			if newFile.endswith('.zip'):
				with ZipFile(f'{UNZIP_FOLDER}/{newFile}', 'r') as zfile:
					no_suffix = newFile[:-4]
					new_dir = f'{UNZIP_FOLDER}/{no_suffix}'
					zfile.extractall(new_dir)

					dirs = next(os.walk(new_dir))[1]
					if no_suffix in dirs:
						new_dir += '/' + no_suffix
					for file in os.listdir(new_dir):
						if file[-3:] == '.py':
							py_file = new_dir + '/' + file
							break
					else:
						py_file = "Extracted file go BRRRR"
				print('unzipped!')
				os.remove(f'{UNZIP_FOLDER}/{newFile}')
			elif newFile.endswith('.py'):
				print('file not zipped')
				py_file = newFile
			else:
				print('invalid file type')
				py_file = "INVALID FILE GO BRR"
			# print(f'{UNZIP_FOLDER}/{newFile}')

			# run the program
			print("CWD:", new_dir)
			cmd = f'python {py_file} < C:\\Users\\Scottie\\Downloads\\ITPUnzip\\ITP115Unzip\\input.txt'
			print(cmd)
			run(cmd, shell=True, cwd=new_dir)
			# run("type Danish.txt", shell=True, cwd=new_dir)

			# run(f'powershell rm "{new_dir}/RestaurantHelper.py"', shell=True)
			# run(f'powershell rm "{new_dir}/Run.py"', shell=True)
			#
			run(f'powershell cp ../deniro.csv "{new_dir}"', shell=True)
			# run(f'powershell cp ../Run.py "{new_dir}"', shell=True)
# if a zip, unzip, place in folder of same name, delete zip

# if not a zip, print something