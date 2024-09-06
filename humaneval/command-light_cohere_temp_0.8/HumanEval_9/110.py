```python
from typing import List
def rolling_max(numbers: List[int]) -> List[int]:
    return [max(numbers[i:], numbers[i+1]) for i in range(len(numbers)-1)]

numbers = [1, 2, 3, 2, 3, 4, 2]
print(rolling_max(numbers))
``` 
This script defines a function called rolling_max that takes a list of integers as input and returns a new list containing the rolling maximum elements. The function uses a specific indexing to get the next element and checks if it's greater than the current maximum element. The result is then the list of increasing maximum elements found in the sequence. 

This is a simple and efficient way to solve the problem of finding the rolling maximum element in a sequence of numbers using Python.