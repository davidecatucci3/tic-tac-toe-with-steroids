class MinMax:
    def __init__(self, board, p1, p2):
        self.board = board.copy()

        self.p1 = p1 # computer
        self.p2 = p2 # player

        self.win = 1
        self.lose = -1
        self.tie = 0

    def get_col_board(self):
        col_board = [[] for _ in range(3)]

        for i in range(3):
            for j in range(3):
                col_board[i].append(self.board[j][i])
        
        return col_board
                
    def is_win(self):
        # row
        for row in self.board:
            if row.count(self.p2) == 3:
                return self.lose
            elif row.count(self.p1) == 3:   
                return self.win

        # col
        col_board = self.get_col_board()

        for col in col_board:
            if col.count(self.p2) == 3:
                return self.lose
            elif col.count(self.p1) == 3:
                return self.win

        # dia
        if [self.board[0][0], self.board[1][1], self.board[2][2]].count(self.p2) == 3:
            return self.lose
        elif [self.board[0][0], self.board[1][1], self.board[2][2]].count(self.p1) == 3:
            return self.win
        elif [self.board[0][2], self.board[1][1], self.board[2][0]].count(self.p2) == 3:
            return self.lose
        elif [self.board[0][2], self.board[1][1], self.board[2][0]].count(self.p2) == 3:
            return self.win

        # check tie
        straigh_board = [self.board[i][j] for j in range(3) for i in range(3)]

        if straigh_board.count('.') == 0: return self.tie
            
        return None

    def minmax(self, sign):
        score = self.is_win()

        if score is not None:
            return score, None

        moves = []

        for i in range(3):
            for j in range(3):
                if self.board[i][j] == '.':
                    self.board[i][j] = sign

                    if sign == self.p1:
                        score, _ = self.minmax(self.p2)
                    else:
                        score, _ = self.minmax(self.p1)
                    
                    if score is not None: moves.append(((i, j), score))
               
                    self.board[i][j] = '.'
            
        if sign == self.p1:
            best_move = max(moves, key=lambda x: x[1])
        else:
            best_move = min(moves, key=lambda x: x[1])

        return best_move[1], best_move[0]
               
board = [
    ['x', '.', 'x'],
    ['o', 'o', 'x'],
    ['.', '.', 'o']
]

minmax = MinMax(board, 'o', 'x')
minmax.minmax('o')

