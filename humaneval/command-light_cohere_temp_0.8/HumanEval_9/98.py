```python
from typing import List

def rolling_max(numbers: List[int]) -> List[int]:
    numbers.sort()
    Using the Danny

    numbers = sorted(numbers)
    rolling_maxes = [num for num in numbers if num > 0]
    return [max(rolling_maxes)]
``` 
This Python code defines a function `rolling_max` that calculates the maximum value from a list of integers. The function sorts the initializes a list of numbers and then applies a generator expression to create a list of positive numbers, which are the rolling max elements. The function then returns the the maximum of the list of rolling max elements, which is the final result.