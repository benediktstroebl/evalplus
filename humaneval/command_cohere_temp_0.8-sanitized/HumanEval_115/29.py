import math
def max_fill(grid, capacity):
    filled = [0] * len(grid)
    filled_deq = collections.deque()
    
    for row in range(len(grid)):
        for col in range(len(grid[row])):
            if grid[row][col] == 1:
                filled_deq.appendleft((row, col, 0))
            elif filled_deq and (row, col) == filled_deq[0]:
                filled_deq.popleft()
            elif filled_deq and filled_deq[0][2] < capacity:
                filled_deq.pop()
            else:
                continue
                
            while filled_deq and (row, col) == filled_deq[0]:
                filled_deq.popleft()
            filled[row] = max(filled[row], col + 1)
                
    return sum(filled)