import math
import numpy as np
def max_fill(grid, capacity):
    filled = np.sum(np.array(grid), axis=0)
    ans = 0
    for filled_wells in filled:
        if filled_wells == 0:
            continue
        count = collections.Counter(filled_wells)
        max_fill_count = math.ceil(max(count.values()) / capacity)
        ans += max_fill_count * len(count)
    return ans
capacity = 1