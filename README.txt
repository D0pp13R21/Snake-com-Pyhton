# Snake Game

Este projeto é um jogo da cobrinha (Snake) desenvolvido em Python usando a biblioteca `pygame`. O jogador controla a cobra que deve comer a comida verde para crescer, enquanto evita colidir com as bordas da tela ou com seu próprio corpo.

## Funcionalidades
- Movimento controlado pelo jogador.
- A cobra cresce cada vez que come a comida.
- O jogo termina se a cobra colidir com seu próprio corpo ou com as bordas da tela.
- Pontuação exibida na parte superior da tela.

## Como Jogar
- **Seta para cima (↑)**: Move a cobra para cima.
- **Seta para baixo (↓)**: Move a cobra para baixo.
- **Seta para esquerda (←)**: Move a cobra para a esquerda.
- **Seta para direita (→)**: Move a cobra para a direita.
  
> **Nota**: Não é possível mover a cobra diretamente para a direção oposta à atual (por exemplo, se estiver indo para cima, não pode ir diretamente para baixo). O jogador deve fazer uma curva para mudar para a direção contrária.

## Tecnologias Utilizadas
- **Python 3.x**
- **Pygame**: Biblioteca usada para criação de jogos 2D.

## Pré-requisitos
Certifique-se de ter o Python e o Pygame instalados em sua máquina.

### Instalação do Python
- Baixe e instale o Python em: https://www.python.org/downloads/

### Instalação do Pygame
Após instalar o Python, execute o seguinte comando para instalar a biblioteca `pygame`:

```bash
pip install pygame
```

## Como Executar o Jogo

1. Clone ou faça o download deste repositório.
2. Navegue até o diretório onde o arquivo principal do jogo (`snake_game.py`) está localizado.
3. Execute o jogo com o seguinte comando:

```bash
python snake_game.py
```

## Regras do Jogo

- A cobra começa no centro da tela, e o jogador deve usar as setas do teclado para controlá-la.
- A cobra cresce cada vez que come a comida (quadrado verde).
- Se a cobra colidir com as bordas da tela ou com seu próprio corpo, o jogo termina.
- A pontuação aumenta em 1 ponto para cada comida coletada.

## Arquitetura do Código

### Funções Principais:

- **rodarJogo()**: Função principal que executa o loop do jogo, atualiza a posição da cobra, gera a comida, e controla a lógica de colisões.
- **selecionarVelocidade(tecla)**: Define a direção da cobra com base na tecla pressionada, impedindo que o jogador mova diretamente para a direção oposta.
- **gerarComida()**: Gera coordenadas aleatórias para a comida na tela.
- **desenharCobra(tamanho, pixels)**: Desenha a cobra com base na lista de pixels que representam seu corpo.
- **desenharComida(tamanho, comidaX, comidaY)**: Desenha a comida na tela.
- **desenharPontos(pontuacao)**: Exibe a pontuação do jogador no topo da tela.

### Variáveis Importantes:
- **velocidadeX e velocidadeY**: Controlam a velocidade e a direção da cobra em cada eixo.
- **largura e altura**: Dimensões da janela do jogo.
- **tamanhoQuadrado**: Tamanho de cada segmento da cobra e da comida.
- **velocidadeJogo**: Controla a velocidade com que a cobra se move no jogo.

## Créditos

Desenvolvido por Lucas Marinho.

