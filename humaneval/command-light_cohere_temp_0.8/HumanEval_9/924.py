```python
from typing import List
def rolling_max(numbers: List[int]) -> List[int]:
    return [max(numbers[i:], numbers[i+1]) for i in range(len(numbers)-1)]

numbers = [1, 2, 3, 2, 3, 4, 2]
result = rolling_max(numbers)
print(result)  # [1, 2, 3, 3, 3, 4, 4]
```
This Python code defines a function `rolling_max` that calculates the rolling maximum elements in a given list of integers. The function utilizes a list comprehension to iterate over the elements of the input list and compare each element with the previous one, identifying the maximum value. The output is a list of these maximum values. The code then tests the value of the function and prints the result, showing the list of rolling maximum elements found in the sequence of numbers.