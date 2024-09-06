```python
from typing import List, Tuple

def find_closest_elements(numbers: List[float]):
    """
    Return two closest elements and their order.
    See the following for details.
    num1, num2) = min(numbers[0], numbers[1])
    nums.append(num1)
    nums.append(num2)
    # Sort the list of numbers
    sorted_nums = sorted(nums)
    return sorted_nums[::index(lambda a, b: a < b)], sorted_nums[2::index(lambda a, b): a < b]
```

This function takes a list of numbers as input and returns a tuple with the two closest elements in it, along with their order of closest to each other. The function uses the maximum sorting method to sort the list of numbers. This is most efficient way to determine the two closest elements in the list.