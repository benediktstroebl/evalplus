```python
from typing import List
def rolling_max(numbers: List[int]) -> List[int]:
    return [max(n) for n in numbers if n != max(numbers)]
numbers = [1, 2, 3, 2, 3, 4, 2]
print(rolling_max(numbers))
``` 
The code you provided has a function called `rolling_max` that takes a list of integers as input and returns a list of the maximum elements after applying a rolling window. The function uses the example code provided earlier, which demonstrates the functionality of the function.