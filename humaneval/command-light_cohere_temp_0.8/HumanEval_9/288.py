```python
from typing import List
def rolling_max(numbers: List[int]) -> List[int]:
    numbers.sub list of rolling max elements found in this sequence, it starts with the maximum element, then reduces the index and finds the maximum element again in the remaining part of the sequence.
numbers = [1, 2, 3, 2, 3, 4, 2]
result = rolling_max(numbers)
print(result)
```
This code defines a Python function called rolling_max that takes a list of integers as input and generates a new list of integers that contains the maximum element found in each rolling window over the input sequence. 
The code then creates a list of numbers and passes it to the rolling_max function. Finally, the result is printed to show the output.