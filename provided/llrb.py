# Implement LLRB a la sedgewick


import sys

RED = 1
BLACK = 0

class Node:
    def __init__(self):
        self.key = None
        self.color = None
        self.left = None
        self.right = None

def valstr(s):
    return int(s.strip())

def tfind(tree, key):
    while tree != None:
        if key < tree.key:
            tree = tree.left
        elif key > tree.key:
            tree = tree.right
        else:
            return tree
    return None

def redq(tree):
    if not tree:
        return False
    else:
        return tree.color == RED
        
def opp_color(c):
    if c == BLACK:
        return RED
    elif c == RED:
        return BLACK

def begin():
    return None

def tinsert(tree, key):
    if not tree:
        new = Node()
        new.key = key
        new.color = RED
        new.left = None
        new.right = None
        return new
    elif key < tree.key:
        # code for key is less than current tree node key
        # replace the 'pass' with your code
        pass
    elif key > tree.key:
        # code for key is greater than current tree node key
        # replace the 'pass' with your code
        pass
    else:
        # code for key is equal to current tree node key 
        # replace the 'pass' with your code
        pass
    # code to fixup tree here

    return tree

def insert(tree, s):
    ntree = tinsert(tree, valstr(s))
    if ntree:
        ntree.color = BLACK
    return ntree

def tdelete(tree, key):
    if not tree:
        return tree
    if not tree.right and not tree.left:
        if key == tree.key:
            return None
        else:
            return tree

    # bulk of your delete code goes here

    return tree

def delete(tree, s):
    key = valstr(s)
    return tdelete(tree, key)

def colorletter(color):
    if color == BLACK:
        return 'b'
    if color == RED:
        return 'r'
    else:
        return '?'

def nodeprint(node):
    print(f'{node.key}{colorletter(node.color)}')
    
def ttprint(tree):
    if tree == None:
        return
    else:
        ttprint(tree.left)
        nodeprint(tree)
        ttprint(tree.right)

def tprint(tree):
    if tree == None:
        print('E')
    else:
        ttprint(tree)
        print()

def dispatch(tree, cmd):
    if cmd[0] == 'B':
        return begin()
    elif cmd[0] == 'I':
        return insert(tree, cmd[2:])
    elif cmd[0] == 'D':
        return delete(tree, cmd[2:])
    elif cmd[0] == 'P':
        tprint(tree)
        return tree
    elif cmd[0] == '\n':
        return tree
        pass
    else:
        print(f'unrecognized command : {cmd}')
        return tree

#
# Run like this:
#  python3 llrb.starter < YOUR_INPUT_FILE
#  answers are printed to the screen
#
if __name__ == '__main__':
    tree = None
    for cmd in sys.stdin:
        tree = dispatch(tree, cmd)
