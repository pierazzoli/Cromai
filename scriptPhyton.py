#######################################################################################
# Author: Eugênio Pierazzoli                                                          #
# Version: 0.3                                                                        #
# Desc: Script em phyton3 para executar tarefas (mensagem em loop por um período de   #
#       tempo)                                                                        #
# Date: 27/01/2020                                                                    #
#######################################################################################

#######################################################################################
#        Task                                                                         #
#######################################################################################
'''O script em python3 precisa abrir um arquivo de nome “pid”,
identificar o seu próprio pid quando estiver rodando e escrevê-lo neste arquivo.
Depois disso, deve rodar um loop por 3 vezes e, a cada iteração, imprimir
“2: I am alive” e aguardar um período de x segundos até fazer a próxima interação.
Ao final deste loop, ele deve imprimir “2: I gonna die now, bye”.'''

#######################################################################################
#        Changelog                                                                    #
#######################################################################################
'''
0.1 versão incial
0.2 implementado o PID e salvar arquivo
0.3 debug para checar o PID
'''

#######################################################################################
#        Start                                                                        #
#######################################################################################


#######################################################################################
#        Variables                                                                    #
#######################################################################################
debug = 0
periodoX = 5
repeticoes = 3
mensagem1 = "“2: I am alive”"
mensagem2 = "“2: I gonna die now, bye”"
nomeArquivo = "pid"

#######################################################################################
#        Imports                                                                      #
#######################################################################################

import os
import sys
import time

#######################################################################################
#        Main                                                                         #
#######################################################################################

#pid
pid = str(os.getpid())
if debug:
    print ("Debug PID = " , pid)
    
f = open(nomeArquivo, "w")
f.write(pid)
f.close()

#loop com mensagem
for x in range(0, repeticoes):
    print (mensagem1)
    time.sleep( periodoX )  

#mensagem final
print (mensagem2)

#######################################################################################
#        EOF                                                                          #
#######################################################################################
