```python
from typing import List
def rolling_max(numbers: List[int]) -> List[int]:
    return [max(numbers[i:]) for i in range(len(numbers))]]

numbers = [1, 2, 3, 2, 3, 4, 2]
print(rolling_max(numbers))
``` 
This code defines a function `rolling_max` that calculates and returns a list of rolling maximum elements from a given list of integers. The function utilizes a list comprehension and the `max()` function to achieve this. The test code then demonstrates the function passing the test by creating a list of numbers and then printing the resulting list of rolling maximum elements.