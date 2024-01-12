<img align="right" alt="Thread Link Logo" width="30%" height="auto" src="https://github.com/GabrielRF/ThreadLinkBot/blob/main/imgs/icon.jpg?raw=true">

# Thread Link Bot

[![Deploy](https://github.com/GabrielRF/ThreadLinkBot/actions/workflows/deploy.yml/badge.svg)](https://github.com/GabrielRF/ThreadLinkBot/actions/workflows/deploy.yml)

## Motivação

> O que esse bot faz?
> 
> Não muito, para ser sincero.

Este bot surgiu após conversa em um grupo de amigos sobre a organização das conversas no Telegram. 

O Telegram, nativamente, possui a organização das conversas em *threads*, porém, o link para a *thread* somente é facilmente acessado a partir de qualquer mensagem **de um grupo público**. Em grupos privados, o acesso à *thread* somente é possível em sua primeira mensagem. O bot foi criado para facilitar tais casos.

## Funcionamento

Sempre que uma mensagem tiver como primeiro caractere `#` e não fizer parte de uma *thread*, o bot enviará o link da *thread* ao grupo, deixando-o mais facilmente acessível a todos.

Caso o bot seja administrador do grupo, o link da *thread* será fixado no grupo, sem que os membros sejam notificados. A mensagem será desafixada quando algum administrador do grupo enviar `/unpin` na *thread*.

![Exemplo de uso do bot](https://github.com/GabrielRF/ThreadLinkBot/assets/7331540/19896dbc-474a-444a-81c7-0054304ea68b)

## Colabore

Toda contribuição é bem vinda! Sem exceção.

## Instalação e Uso

O bot é um script Python que funciona usando *polling*. Ou seja, não exige muito esforço para funcionar. O único requisito é a biblioteca [PyTelegramBotAPI](https://github.com/eternnoir/pytelegrambotapi), que pode ser instalada pelo comando:

```
pip install pytelegrambotapi
```

Crie um arquivo chamado `token.conf` cujo conteúdo seja o token de seu bot e execute o sript python.

```
python bot.py
```
