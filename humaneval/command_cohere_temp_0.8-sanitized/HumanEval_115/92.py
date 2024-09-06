import math
import collections
def max_fill(grid, capacity):
    filled_buckets = collections.deque()

    for row in grid:
        filled_buckets.appendleft(0)

        for bucket in row:
            if bucket:
                filled_buckets.appendleft(filled_buckets[0] + 1)
                if len(filled_buckets) > capacity:
                    filled_buckets.pop()

    return len(filled_buckets)
capacity = 1