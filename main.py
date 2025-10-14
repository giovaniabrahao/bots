import pyautogui
import webbrowser
import openpyxl
from urllib.parse import quote
from time import sleep

#abrir whatsapp web
webbrowser.open('https://web.whatsapp.com/')
sleep(30)

#Deve-se criar uma planinha com as informações a serem personalizadas na planilha

#abrindo arquivo Excel/ importante ter um arquivo com o nome book4.xlsx dentro da pasta do projeto
workbook = openpyxl.load_workbook('book4.xlsx')
#acessando a sheet correta / é necessário que a planilha tenha uma aba com o nome "Planilha1"
worksheet = workbook['Planilha1']

#percorrer as linhas da planilha
for linha in worksheet.iter_rows(min_row=2):
    #extração de informações importantes
    cliente = linha[0].value
    placa = linha[1].value
    modelo = linha[2].value
    contato = linha[3].value
    empresa = linha[4].value
    mensagem = (f'''Atenção, essa não é uma mensagem automática
Olá, {cliente}.

Me chamo Renan e sou da equipe de Gestão e Segurança de Frotas da {empresa}. 🚗
Estou entrando em contato referente ao veículo locado:

* Placa: {placa}
* Modelo: {modelo}

Identificamos pendências contratuais vinculadas a esse veículo, o que pode resultar em medidas de retomada do bem.
Nosso objetivo é resolver essa situação da forma mais rápida e prática possível. Você pode comparecer à agência para regularização ou, se preferir, alinhar a devolução imediata do veículo.

Se o pagamento já foi efetuado, por gentileza, envie o comprovante para atualização em nosso sistema.

Agradecemos sua atenção e aguardamos seu retorno.''')

    #criar links personalizado para envio das mensagens
    try:

        link_message = f'https://web.whatsapp.com/send?phone={contato}&text={quote(mensagem)}'
        #abrir conversa
        webbrowser.open(link_message)
        sleep(30)

        #localizando botão de envio
        seta = pyautogui.locateCenterOnScreen('seta.png', confidence=0.8)
        sleep(5)

        if seta: #verificar se o botão foi encontrado
            pyautogui.click(seta[0], seta[1])
            sleep(8)
            pyautogui.hotkey('ctrl', 'w')
            sleep(2)
        else:
            print(f"Botão de enviar não encontrado para {contato}")
            print("Tentativa de envio com o declado falhou, iniciando tentativa com o mouse")

    except Exception as e:

        print(f"Envio por referencia do mouse falhou para o contato {contato} tentando com o teclado")
        '''pyautogui.press('tab')
        #sleep(5)'''
        pyautogui.press('enter')
        sleep(8)
        pyautogui.hotkey('ctrl', 'w')
        sleep(8)

        if contato == "":
            pyautogui.press('f5')
        else:
            continue

    except Exception as e:
        if contato == "":
            print(f"Contato de {contato} não existe")
            continue
        else:
            print("Ocorreu um erro com o contato de destino...")
            continue
