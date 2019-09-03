import os, time
from zipfile import ZipFile

DOWNLOADS_FOLDER = 'C:/Users/xboxl/Downloads'

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
	downloads = os.listdir(DOWNLOADS_FOLDER)
	if len(downloads) != numDownloads:
		time.sleep(1) # to ignore temporary files associated with downloads
		downloads = os.listdir(DOWNLOADS_FOLDER)
		if len(downloads) != numDownloads:
			print('got this far')
			# new download
			downloads = set(downloads)
			newFile = list(downloads.difference(initialDownloads))[0]
			print(f'Detected new file: {newFile}')

			# move file from downloads to ITPUnzip folder
			os.rename(f'{DOWNLOADS_FOLDER}/{newFile}', f'{UNZIP_FOLDER}/{newFile}')
			
			# see if it is a zip or a py or something else
			if newFile.endswith('.zip'):
				with ZipFile(f'{UNZIP_FOLDER}/{newFile}', 'r') as zfile:
					zfile.extractall(f'{UNZIP_FOLDER}/{newFile[:-4]}')
				print('unzipped!')
				os.remove(f'{UNZIP_FOLDER}/{newFile}')
			elif newFile.endswith('.py'):
				print('file not zipped')
			else:
				print('invalid file type')
# if a zip, unzip, place in folder of same name, delete zip

# if not a zip, print something