Here's the code:
```python
from typing import List, Tuple

def find_closest_elements(numbers: List[float]):
    # initializing the first element as closest
    closest, second_closest = (numbers[0], numbers[1])

    # sort the list of numbers based on the comparison of their elements with the closest and second_closest
    sorted_numbers = sorted((numbers, numbers[::-1]), key=lambda a: a if a == closest else a == second_closest else -0)

    # take the first element of the sorted list as the second closest
    second_closest = sorted_numbers[0]

    return (closest, second_closest)

# test cases
numbers = [1.0, 2.0, 3.0, 4.0, 2]
(1.0, 2.0, 3.0, 4) is closest

```

Note that the provided solution is a good starting point for this problem, but it may need to be optimized or optimized to improve the performance. If you are looking for a more efficient solution, you can try other algorithms such as binary search, sorting, or dynamic programming.