# 🤖 Bots de Automação em Python

## 🎯 Objetivo do Projeto
Este projeto consiste em um bot automatizado desenvolvido em Python para **disparo massivo de mensagens via WhatsApp Web**, utilizando dados de contato e conteúdo extraídos de uma planilha Excel. O algoritmo é ideal para estudos em automação de processos e comunicação.

## ✨ Funcionalidades Principais
* Abertura e controle do navegador (Chrome/Edge).
* Carregamento de dados de contatos e variáveis a partir de um arquivo `book4.xlsx`.
* Iteração sobre as linhas do Excel para personalizar e enviar mensagens.
* Múltiplas tentativas de envio (referência visual via `pyautogui` e `hotkeys`).
* Geração de um relatório `.CSV` com os contatos que não receberam a mensagem.

## ⚠️ Pré-Requisitos e Precauções
Para a execução correta do algoritmo, o usuário deve:

1.  **Bibliotecas:** Certificar-se de que todas as bibliotecas necessárias (como `selenium`, `pandas`, `pyautogui`, etc.) estão instaladas.
2.  **Login no WhatsApp Web:** O primeiro login na sessão do WhatsApp Web deve ser feito **manualmente** pelo usuário antes da execução do script, garantindo que a sessão esteja ativa.
3.  **Planilha de Dados:** O arquivo de dados deve ser nomeado como `book4.xlsx` e estar no diretório especificado, contendo as colunas com as informações (número de telefone, variáveis personalizadas, etc.).
4.  **Máquina Desocupada:** Durante a execução, a máquina deve estar **desocupada** e sem uso secundário, pois o algoritmo simula interações de mouse e teclado que podem ser interrompidas por interferência do usuário.

## 🛠️ Pontos de Customização
O código foi estruturado para permitir personalizações sem a necessidade de alterar a lógica central do algoritmo. Os pontos customizáveis são:

| Elemento | Descrição | Onde Alterar |
| :--- | :--- | :--- |
| **Arquivo Excel** | Nome e diretório do arquivo de entrada de dados. | Linhas de carregamento do arquivo. |
| **Colunas** | Nomes das colunas da planilha (`Sheet`) que serão lidas. | Variáveis de leitura do Pandas. |
| **Mensagem Padrão** | O texto base da mensagem a ser enviada. | Variável de definição da mensagem. |
| **Relatório de Erros** | Nome do arquivo `.CSV` de saída. | Linhas finais do algoritmo. |

> 📌 **Importante:** Altere apenas as informações customizáveis (textos, nomes de colunas, nomes de arquivos), evitando modificar a estrutura de comandos do algoritmo.

## 🛡️ Tratamento de Erros e Tentativas de Envio
O algoritmo foi projetado com robustez para lidar com falhas no processo de envio, utilizando um sistema de **duas tentativas** para cada contato, após a correta abertura do link personalizado:

1.  **Tentativa 1 (Referência Visual):** A biblioteca `pyautogui` tentará localizar a imagem do ícone de envio (`.png` no diretório) para simular um clique de mouse no botão.
2.  **Tentativa 2 (Hotkeys):** Se a primeira tentativa falhar, o algoritmo simulará o uso de atalhos de teclado (pressionar `Tab` e, em seguida, `Enter`).

Em ambos os casos de envio (sucesso ou falha), o algoritmo fechará a aba atual (simulando `CTRL+W`) e abrirá uma nova para seguir com a próxima iteração.

### Relatório Final
Ao término de todas as iterações, será gerado um arquivo `.CSV` indicando os contatos que não receberam a mensagem, sem distinguir o motivo da falha. Esta funcionalidade também é customizável, caso o usuário tenha a capacidade de realizar alterações lógicas.
