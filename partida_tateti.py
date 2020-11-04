class Partida_Tateti():

    def __init__(self, board={}, piece='', valid=[]):
        self.board =   {'1,1':'', '1,2':'', '1,3':'',
                        '2,1':'', '2,2':'', '2,3':'',
                        '3,1':'', '3,2':'', '3,3':''}
        self.piece = piece
        self.valid = valid

    @property
    def board(self):
        return self._board

    @board.setter
    def board(self, board):
        self._board = board 

    @property
    def piece(self):
        return self._piece

    @piece.setter
    def piece(self, piece):
        self._piece = piece.upper()

    @property
    def valid(self):
        return self._valid

    @valid.setter
    def valid(self, valid):
        self._valid = valid