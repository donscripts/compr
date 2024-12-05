import os
import sys
import zipfile
import tarfile
import rarfile

arquivo= ' '.join(sys.argv[1:])
if arquivo:
	if os.path.exists(arquivo):#se existir
		if os.path.isfile(arquivo):#se for um arquivo
			partes= os.path.splitext(arquivo)
			match partes[1]:
				case '.zip':
					z= zipfile.ZipFile(arquivo, 'r')
					lista= z.namelist()
					for item in lista:
						if item.endswith('/'):
							print(f'[ {item} ] [diretorio]')
						else:
							print(f'[ {item} ] [arquivo]')
				case '.tar':
					t= tarfile.open(arquivo, 'r:*')
					lista= t.getnames()
					for item in lista:
						if item.endswith('/'):
							print(f'[ {item} ] [diretorio]')
						else:
							print(f'[ {item} ] [arquivo]')
				case '.rar':
					r= rarfile.RarFile(arquivo)
					lista= r.namelist()
					for item in lista:
						if item.endswith('/'):
							print(f'[ {item} ] [diretorio]')
						else:
							print(f'[ {item} ] [arquivo]')
				case _:
					print(f'Sem suporte para: [{partes[1]}]')
		else: print('O item nao e um arquivo')
	else: print('O item nao existe')
else: print('Voce deve informar o nome do arquivo compremido')

os.system('Pause')