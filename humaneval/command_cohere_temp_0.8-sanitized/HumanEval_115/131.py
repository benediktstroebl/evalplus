import math
import collections
def max_fill(grid, capacity):
    filled_deque = collections.deque() # container to efficiently calculate filled slots in a given row
    total_fill = 0

    # iterate through each row in the grid
    for row in grid:
        filled = 0 # counter to track filled slots in the current row

        # iterate through each column in the current row
        for col in row:
            if col == 1:
                filled += 1

                # check if this fill can be efficiently combined with previous fills in the same row
                while filled_deque and filled_deque[-1] == filled:
                    filled_deque.pop()
                    filled += 1

                if filled > capacity:
                    total_fill += (filled // capacity) - 1
                else:
                    total_fill += 1

            else:
                # add a sentinel value to mark end of filled slots in current row
                filled_deque.append(float('inf'))

        # add a sentinel value to mark end of filled slots in current row
        filled_deque.append(float('inf'))

    return total_fill
capacity = 1