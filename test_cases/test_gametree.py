from board import *
from config import *
from gametree import *
from heuristic import *
from logger import *


board_file = open("board.txt",'r')
# index = 0
# for line in board_file.readlines():
#     #current player
#     print("--------------------begin-------------------")
#     print(index)
#     cur = (index % 2) + 1
#     print("Current Player is {}. Black = 1 White = 2".format(cur))
#     board_list = convert_string_to_board(line)
#     current_board = Board(board_list)
#     print("Testing board")
#     current_board.print_board()
#     #Black player is the max in this testcase
#     print("Reg minimax")
#     current_node = Node(current_board,cur)
#     value = minimax(current_node,0,3,heuristic_1,current_node.curPlayer,Piece.BLACK,Piece.WHITE)
#     print(value)
#     print("Minimax with Alpha Beta")
#     value = alphabeta_minimax(current_node,0,3,heuristic_1,current_node.curPlayer,Piece.BLACK,Piece.WHITE,-1000000,1000000)
#     print(value)
#
#     print("Testing its children")
#     for possible_move in current_board.get_possible_move(cur):
#         new_node = deepcopy(current_node)
#         new_node.board.make_move(possible_move,cur)
#         new_node.board.print_board()
#         opponent = new_node.board.get_opposite_color(cur)
#         new_node.curPlayer = opponent
#         print("Max Player : {}".format(cur))
#         print("Min Player : {}".format(opponent))
#         value = alphabeta_minimax(new_node,0,2,heuristic_5,opponent,cur,opponent,-1000000,1000000)
#         print(value)
#     print("--------------------end-------------------")
#     index += 1

index = 5
line = "3333333333333333333333333331233333312333333123333333113333333133"
print("--------------------begin-------------------")
print(index)
cur = (index % 2) + 1
print("Current Player is {}. Black = 1 White = 2".format(cur))
board_list = convert_string_to_board(line)
current_board = Board(board_list)
print("Testing board")
current_board.print_board()
#Black player is the max in this testcase
#print("Reg minimax")
current_node = Node(current_board,cur)
#value = minimax(current_node,0,3,heuristic_1,current_node.curPlayer,Piece.BLACK,Piece.WHITE)
#print(value)
print("Minimax with Alpha Beta")
value = alphabeta_minimax(current_node,0,4,heuristic_7,Piece.WHITE,Piece.WHITE,Piece.BLACK,-1000000,1000000)
print(value)
print(current_board.get_possible_move(Piece.WHITE))

print("--------------Testing its children-------------------")
for possible_move in current_board.get_possible_move(Piece.WHITE):
    new_node = deepcopy(current_node)
    new_node.board.make_move(possible_move,Piece.WHITE)
    new_node.board.print_board()
    opponent = new_node.board.get_opposite_color(Piece.WHITE)
    new_node.curPlayer = opponent
    print("Max Player : {}".format(cur))
    print("Min Player : {}".format(opponent))
    value = alphabeta_minimax(new_node,1,4,heuristic_7,Piece.BLACK,Piece.WHITE,Piece.BLACK,-1000000,1000000)
    print(value)
    # print("------------------Testing its grandchildren-----------")
    # for possible_move_2 in current_board.get_possible_move(Piece.BLACK):
    #     new_node_2 = deepcopy(new_node)
    #     new_node_2.board.make_move(possible_move_2,Piece.BLACK)
    #     new_node_2.board.print_board()
    #     value_2 = alphabeta_minimax(new_node,2,4,heuristic_7,Piece.WHITE,Piece.WHITE,Piece.BLACK,-1000000,1000000)
    #     print(value)
    #print("-----------------finish testing children------------")
print("--------------------end other layer-------------------")
index += 1