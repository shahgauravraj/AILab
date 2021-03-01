import math
import random

def minimax(depth, nodeIndex, maxturn, alpha, beta):
    if depth == Depth:
        return values[nodeIndex]
    if maxturn:
        best = minimum
        for i in range(Children):
            val = minimax(depth + 1, nodeIndex * Children + i, False, alpha, beta)
            best = max(best, val)
            alpha = max(alpha, best)
            if beta <= alpha:
                break
            print(depth + 1, nodeIndex * Children + i, best, val)
        return best
    else :
        best = maximum
        for i in range(Children):
            val = minimax(depth + 1, nodeIndex * Children + i, True, alpha, beta)
            best = min(best, val)
            beta = min(beta, best)
            if beta <= alpha:
                break
            print(depth + 1, nodeIndex * Children + i, best, val)
        return best

# Driver Code

maximum, minimum = 1000, -1000
values = random.sample(range(-2, 10), 8)

# values = [3, 5, 6, 9, 1, 2, 0, -1]

print(str(values))
Children = 2
Depth = math.log(len(values), Children)

print("The optimal value is :", minimax(0, 0, True, minimum, maximum))