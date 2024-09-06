```python
from typing import List

def rolling_max(numbers: List[int]) -> List[int]:
    """
    From a given list of integers, generate a list of rolling maximum elements found until the given moment
    in the sequence.
    Args:
        numbers (List[int]): Input list of integers.
    Returns:  List[int]: Output list of rolling maximum elements
    """
    max_roll = 0
    rolling_max_list = [0]

    for num in numbers:
        if num > max_roll:
            max_roll = num
        rolling_max_list.append(max_roll)
        rolling_max_list.append(num)

    return rolling_max_list

# Test cases
numbers = [1, 2, 3, 4, 5]
result = rolling_max(numbers)
print(result)

numbers = [2, 3, 4, 5, 6]
result = rolling_max(numbers)
print(result)

numbers = [0, 1, 2]
result = rolling_max(numbers)
print(result)
```
This code defines a function `rolling_max` that calculates the rolling maximum elements in a given list of integers. The function uses a type hint for the input parameter `numbers` to ensure the correct type is passed. The function then uses a `List[int]` to create a list of rolling maximum elements and a `List[int]` to create a list of numbers. The `for` loop iterates over the numbers in the list and compares each element with the current maximum value to update the rolling maximum value. Finally, the function returns the list of rolling maximum elements. The test cases show how the use of the `rolling_max` function with different input lists, and the output is printed to the console.