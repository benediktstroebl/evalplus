Here's the solution:
```python
from typing import List, Tuple

def find_closest_elements(numbers: List[float]):
    # initialize two variables
    min_num = float('inf')
    max_num = 0
    # loop through list of numbers
    for num in numbers:
        # find minimum and maximum number
        min_num = min(min_num, num)
        max_num = max(max_num, num)
    # return the two numbers that are the closest to each other
    return (min_num, max_num)

```
The function takes a list of numbers as input and returns a tuple containing the two closest numbers. The function uses a maximum-difference algorithm to find the closest numbers and selects the smaller number as the first element of the tuple.

Note that the function assumes that the list contains at least two elements. The function also uses the minimum and maximum functions from the typing module to efficiently find the closest numbers.

You can use this function to solve the problem by passing your own list of numbers as an argument.