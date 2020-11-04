class TaTeTi():

    def ingresar_xy(self,piece):
        letra = self.piece
        if letra == '':
            while not (letra == 'X' or letra == 'O'):
                print ('¿Que ficha quieres usar X o O?')
                letra = input().upper()
    
    def game(self):
        print(self)
        while not self.win() and len(self.valid) > 0:
            self.board[self.input_position()] = ' ' + self.piece + ' '
            print(self)
            winner = self.piece
            self.piece = 'o' if self.piece == 'x' else 'x'
        if len(self.valid) == 0:
            winner = 'Ninguno'
        return winner



if __name__ == '__main__':
    game = TaTeTi()

    print('Ganó ' + game.game())
