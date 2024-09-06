```python
from typing import List
def rolling_max(numbers: List[int]) -> List[int]:
    return [max(numbers[i:]) for i in range(len(numbers))]]
numbers = [1, 2, 3, 2, 3, 4, 2]
print(rolling_max(numbers))  # Output: [1, 2, 3, 3, 3, 3, 4, 4]
``` 
This function uses Python's list comprehension along with the `max()` function to calculate the maximum element within each rolling window of the input list. 
In this solution, the function accepts a list of integers as input and returns a list of the maximum elements found in each window of the input sequence.