from copy import copy
import csv
from datetime import datetime
from lib2to3.pgen2.token import NEWLINE
from locale import format_string
import string
from traceback import print_list
import numpy as np
from prompt_toolkit import print_formatted_text

#---------------------------------------------------------------------------------------------

#-----------------------------------COMANDOS BAT----------------------------------------------

#---------------------------------------------------------------------------------------------
#INCLUIR HOST
#xcopy \\172.20.1.9\prog$\hosts-2022-05-04.txt \\fat1\c$\windows\system32\drivers\etc\hosts /y
#---------------------------------------------------------------------------------------------
#INCLUIR ATALHOS
#xcopy \\172.20.1.9\prog$\HSVP_atalhos\Win7\64\* \\fat1\c$\Users\Public\Desktop\* /y
#---------------------------------------------------------------------------------------------
#ATUALIZAR PASTA TASY NO C DO USUARIO
#xcopy \\172.20.1.9\prog$\Tasy\Tasy\*  \\fat72\c$\ProgramFiles\Tasy\* /y
#---------------------------------------------------------------------------------------------
#ATUALIZA ICONES
#xcopy \\172.20.1.9\prog$\HSVP_icones\* \\fat1\c$\ProgramFiles\HSVP_icones\* /y
#----------------------------------------------------------------------------------------------
#INSERE CREDENCIAL
#cmdkey /add:fat3 /user:fat\hsvp /pass:09adm#14
#----------------------------------------------------------------------------------------------
#DELETA ARQUIVO
#del \\fat1\c$\Users\Public\Desktop\"TASY [produção 3].Lnk" 
#  OBS: arquivos com espaço em branco deverão ser entre aspas
#----------------------------------------------------------------------------------------------
arquivo = open('principal.csv')
linhas = csv.DictReader(arquivo)
file = open("atualizaParque.bat", "w+")
saida = open("c:\saida.txt", 'w+')
#saida.write('cd c:\ ')
#------------------------------------
#FUNÇÃO INCLUIR LINHA NO BAT
#------------------------------------
def incluir_linha(pc, conteudo):
    #file.write(conteudo +'\n')
    file.write('@echo NOME PC:' + pc +'\n' + conteudo +'\n')
    #saida.write(r'NOME PC:' + pc +'\n')
     
def diaAtual():
    return datetime.today().strftime('%d')
#--------------------------------------------------------------
#LEITURA E GRAVAÇÃO ARQUIVO BAT    
#-------------------------------------------------------------- 
for linha in linhas:
#----------------------------------------------------------insere credencial no proprio pc  ----------------------------------------------------
#    insereCredencial = r'cmdkey /add:{host} /user:{ip}\hsvp /pass:09adm#14'.format(ip = linha['ip'] , host = linha['host'])   
#    arrayCred= np.array(insereCredencial)
#    content = str(arrayCred)
#    incluir_linha(linha['host'],content)
#----------------------------------------------------------atualiza host   ----------------------------------------------------
#    atualizaHost = r'copy \\172.20.1.9\prog$\hosts-2022-05-'+ diaAtual() +'.txt \\\{host}\c$\windows\system32\drivers\etc\hosts /y'.format(host = linha['host'])   
#    arrayHost = np.array(atualizaHost)
#    content = str(arrayHost)
#    incluir_linha(linha['host'],content + ' >> c:\saida.txt')
#-------------------------------------------- atualiza icones ------------------------------------------------------------------
    atualizaIcones = r'xcopy \\172.20.1.9\prog$\HSVP_icones\* \\{host}\c$\ProgramFiles\HSVP_icones\* /y '.format(host = linha['host'])
    arrayIcones = np.array(atualizaIcones)
    content = str(arrayIcones)
    incluir_linha(linha['host'], content)  
#-----------------------------------------------------atualiza PASTA TASY NO C  -------------------------------------------------
    insereTasy = r'xcopy \\172.20.1.9\prog$\Tasy\Tasy\* \\{host1}\c$\ProgramFiles\Tasy\* /y'.format(host1 = linha['host'])   
    arrayTasy = np.array(insereTasy)
    content1 = str(arrayTasy)
    incluir_linha(linha['host'],content1  + ' >> c:\saida.txt')
#--------------- ---------------------------------------  atualiza atalhos   ----------------------------------------------------------------------
    insereAtalhosVariados = r'xcopy \\172.20.1.9\prog$\HSVP_atalhos\Win7\64\* \\{host2}\c$\Users\Public\Desktop\* /y'.format(host2 = linha['host'])   
    arrayAtalho = np.array(insereAtalhosVariados)
    content2 = str(arrayAtalho)
    incluir_linha(linha['host'],content2)
#--------------- ---------------------------------------  DELETAR ATALHO   ----------------------------------------------------------------------
    deletarAtalho = r'DEL \\{host3}\c$\Users\Public\Desktop\"TASY [produção 3].Lnk"'.format(host3 = linha['host'])   
    arrayDeletarAtalho = np.array(deletarAtalho)
    content3 = str(arrayDeletarAtalho)
    incluir_linha(linha['host'],content3)    
#----------------------------------------------------------------------------------------------------------------------------------------------------
else:
    print('Terminou a leitura e gravação do arquivo!!!!!!')
#file.write('\n' + '@echo Arquivo gerado em : C:\Users\Public\Desktop\saida.txt '+'\n')
    file.write('pause') 
#FIM
