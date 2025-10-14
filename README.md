# bots
Bots automarizados criados em Python

Bot criado para estudos utlizando bibliotecas voltadas para automação de processos com python.

A ideia desse algoritmo é permitir ao usuario realizar disparos de mensagens via whatsapp WEB automaticamente a partir de uma planilha de excel contendo as informações que o usuario designar.

<h1>Precauções com o código</h1>
O codigo em questão foi construido em partes bem definidas, sendo elas:
<ul>
    <ol>Importação das bibliotecas necessárias</ol>
    <ol>Abertura do navegador padrão</ol>
    <ol>Abertura de um Whatsapp web já previamente estabelicido, ou seja o usuario deve fazer o prim<br>
    login manualmente</ol>
    <ol>Após isso o algoritimo irá buscar e carregar o arquivo excel chamado book4.xlsx no diretório<br>
    Este ponto o usuario poderá criar um arquivo com este nome ou poderá alterar o nome<br>
    do arquivo que será localizado, bem como o diretório diretamente no código</ol>
    <ol>Após localizar o arquivo e a sheet correta designada dentro do das linhas superiores, o<br>
    o algoritmo irá começar a ler as linhas e realizar as iterações de envios de mensagens,<br>
    importe ressaltar que neste ponto o código já possui os nomes das colunas pré estabelecidas que pode
    ser alteradas pelo usuario de acordo com a sua necessidade ou contexto, incluidon ou removendo<br>
    colunas da planilha e alterando a mensagem padrão.</ol>
</ul>
Portanto se faz necessário atenção com as alterações, evitando alterar o código do algoritmo, reservando-se apenas a alterar as informações customizaveis, como texto padrão que será enviado, numero e ordem das colunas
que irão aparecer na mensagem padrão

Também é importe que durante a execução do algoritmo a maquina esteja desocupada e que não seja feito nenhum tipo de uso secundario

Ao término da execução do algoritmo será gerado um arquivo .CSV indicando os contatos que não receberam a mensagem, sem distinguir o motivo, função essa que também poderá ser alterada pelo usuario caso o mesmo tenha
capacidade logica para realizar alterações no código sem comprometer a estrutura padrão.

<h3>Tratamentos de erros</h3>
O algoritmo funcionará com duas tentativas de envio para cada contato a partir do momento que o link personalizado abra corretamente, sendo elas:

Envio por referencia de botão, dentro do diretorio há um arquivo .png com o icone de envio, a qual o biblioteca <b>pyautogui</b> tentará localizar para simular um click de mouse no botão a partir da referencia visual.
Após isso será feita a verificação do envio do botão, caso retorne como negativo então o algoritmo tentará executar a segunda forma, que é através do uso de hotkeys, onde o algoritmo irá simular o toque nas teclas Tab e na sequencia enter.
Para ambos os casos o algoritmo irá fechar a aba principal simulando a hotkey CTRL+W para então abrir uma nova e dar seguimento nas iterações.

Ao termino da execução de todas as iterações será gerado o arquivo .CSV como relatório de erros.
