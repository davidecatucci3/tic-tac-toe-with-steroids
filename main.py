import random

from minmax import MinMax

# answer
answer = {
    "intro": "Jucamo, che vulissi, a X o la O? ",
    "select_x": "E si nu cazz'i butirro pure tu eh?!",
    "select_o": "E si nu cazz'i buttigghiuno",
    "error_selecting_sign": "Cumbà statti accurto ca ti tagghiu i mani",
    "no_game": "T' accummugghio e t'arravugghio n'faccia allu muro, cazz'i tambruno fricato",
    "select_pos": "Combacri addu la nziccamo sta %s? ",
    "error_selecting_pos_number": "Ma cu t'ambarato, i vu minde dui numeri justi ingegné? ",
    "error_selecting_pos_busy": "Allora si cugghiuno, vida i cangia posto prima ca ti frico nu suttamusso",
    "win": "Hai vinto, Tantu piaciro allu cazzu dotto, Ama rifa? ",
    "lose": "Hai perso, T'avissa frica n'gapo stu cazz'i juco",
    "tie": "Abbiamo pareggiato, ama rijuca'? ",
    "rematch_yes": "Allora t'avia strappa i ricchie a muzzichi",
    "rematch_no": "T' agghia frica na furciddata 'ndi spaddre, si pop nu cazz'i stuzzuno"
}

# tris game
class Tris:
    def __init__(self):
        self.board = [['.' for _ in range(3)] for _ in range(3)]

        self.p1 = '' # computer
        self.p2 = '' # player
        
        self.winner = ''
    
    def print_board(self):
        print(' ')

        for i in self.board:
            for j in i:
                print(j, end=' ')
            
            print(' ')
    
    def select_sign(self):
        print(' ')
        self.p2 = input(answer['intro']).lower().strip()
        self.p1 = 'x' if self.p2 == 'o' else 'o'
        print(' ')
        if self.p2 == 'x': 
            print(answer['select_x'])
        elif self.p2 == 'o':
            print(answer['select_o'])
        elif self.p2 == 'no':
            print(answer['no_game'])

            return False
        else:
            print(answer['error_selecting_sign'])

            self.select_sign()
        
        return True
    
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
                self.winner = self.p2

                return True
            elif row.count(self.p1) == 3:   
                self.winner = self.p1

                return True

        # col
        col_board = self.get_col_board()

        for col in col_board:
            if col.count(self.p2) == 3:
                self.winner = self.p2

                return True
            elif col.count(self.p1) == 3:
                self.winner = self.p1

                return True

        # dia
        if [self.board[0][0], self.board[1][1], self.board[2][2]].count(self.p2) == 3:
            self.winner = self.p2

            return True
        elif [self.board[0][0], self.board[1][1], self.board[2][2]].count(self.p1) == 3:
            self.winner = self.p1
            
            return True
        elif [self.board[0][2], self.board[1][1], self.board[2][0]].count(self.p2) == 3:
            self.winner = self.p2

            return True
        elif [self.board[0][2], self.board[1][1], self.board[2][0]].count(self.p1) == 3:
            self.winner = self.p1

            return True

        # check tie
        straigh_board = [self.board[i][j] for j in range(3) for i in range(3)]

        if straigh_board.count('.') == 0: return True
            
        return False

    def p2_turn(self):
        print(' ')
        pos = input(answer['select_pos'] % self.p2 + ' ').strip()
       
        pos = pos.split(' ')
        pos = list(map(lambda x: int(x), pos))

        row, col = pos

        # pos exceeded range board
        if row < 0 or row > 2 or col < 0 or col > 2:
            print(' ')
            print(answer['error_selecting_pos_number'])

            self.p2_turn()
        else:
            if self.board[row][col] == '.':
                self.board[row][col] = self.p2
            else:
                print(answer['error_selecting_pos_busy'])

                self.p2_turn()
    
    def p1_turn(self, ai=False):
        # not use minmax algorithm
        if not ai:
            pos = [random.randrange(0, 3), random.randrange(0, 3)]

            row, col = pos

            while self.board[row][col] != '.':
                pos = [random.randrange(0, 3), random.randrange(0, 3)]

                row, col = pos

            self.board[row][col] = self.p1
        else:
            minmax = MinMax(self.board, self.p1, self.p2)

            _, pos = minmax.minmax(self.p1)

            row, col = pos

            self.board[row][col] = self.p1

    def rematch(self):
        # reset all
        self.board = [['.' for _ in range(3)] for _ in range(3)]

        self.p1 = '' # computer
        self.p2 = '' # player
        
        self.winner = ''

        self.play()

    def play(self):
        if self.select_sign(): # enter sign (x / o)
            while True: # check if someone has won
                self.print_board() # print board

                self.p2_turn() # turn of player

                if self.is_win(): break # check win

                self.p1_turn(True) # turn of computer 

                if self.is_win(): break # check win
            
            self.print_board() # mark the winner sign

            # print winner
            print(' ')
            if self.winner == self.p2:
                is_rematch = input(answer['win']).strip()
                print(' ')
                if is_rematch == 'si': 
                    print(answer['rematch_yes'])
                    
                    self.rematch()
                elif is_rematch == 'no': 
                    print(answer['rematch_no'])
            elif self.winner == self.p1:
                print(answer['lose'])
            else:
                is_rematch = input(answer['tie']).strip()
                print(' ')
                if is_rematch == 'si': 
                    print(answer['rematch_yes'])
                    
                    self.rematch()
                elif is_rematch == 'no': 
                    print(answer['rematch_no'])

tris = Tris()

tris.play()
