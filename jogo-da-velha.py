import random


class JogoDaVelha:

    def __init__(self):
        self.board = []

    def create_board(self):
        for i in range(3):
            linha = []
            for j in range(3):
                linha.append('-')
            self.board.append(linha)

    def get_random_first_player(self):
        return random.randint(0, 1)

    def fix_spot(self, linha, col, jogador):
        self.board[linha][col] = jogador

    def is_player_win(self, jogador):
        ganhou = None

        n = len(self.board)

        for i in range(n):
            ganhou = True
            for j in range(n):
                if self.board[i][j] != jogador:
                    ganhou = False
                    break
            if ganhou:
                return ganhou

        for i in range(n):
            ganhou = True
            for j in range(n):
                if self.board[j][i] != jogador:
                    ganhou = False
                    break
            if ganhou:
                return ganhou

        ganhou = True
        for i in range(n):
            if self.board[i][i] != jogador:
                ganhou = False
                break
        if ganhou:
            return ganhou

        ganhou = True
        for i in range(n):
            if self.board[i][n - 1 - i] != jogador:
                ganhou = False
                break
        if ganhou:
            return ganhou
        return False

        for linha in self.board:
            for item in linha:
                if item == '-':
                    return False
        return True

    def is_board_filled(self):
        for linha in self.board:
            for item in linha:
                if item == '-':
                    return False
        return True

    def swap_player_turn(self, jogador):
        return 'X' if jogador == 'O' else 'O'

    def show_board(self):
        for linha in self.board:
            for item in linha:
                print(item, end=" ")
            print()

    def start(self):
        self.create_board()

        jogador = 'X' if self.get_random_first_player() == 1 else 'O'
        while True:
            print(f"Vez do jogador {jogador}")

            self.show_board()

            linha, col = list(
                map(int, input("Insira linha e coluna desejadas: ").split()))
            print()

            self.fix_spot(linha - 1, col - 1, jogador)

            if self.is_player_win(jogador):
                print(f"Jogador {jogador} ganhou!")
                break

            if self.is_board_filled():
                print("Deu velha!")
                break

            jogador = self.swap_player_turn(jogador)

        print()
        self.show_board()


tic_tac_toe = JogoDaVelha()
tic_tac_toe.start()