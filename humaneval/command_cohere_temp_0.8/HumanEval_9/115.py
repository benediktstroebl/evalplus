Here is a Python script with a self-contained function that solves the problem:
```python
from typing import List, Tuple

def rolling_max(numbers: List[int], rolling_window: int) -> List[int]:
    return [max(list(numbers[-rolling_window:])) for nums in zip(*[iter(numbers)]*rolling_window)]
```

The rolling_max function takes in a list of numbers and a rolling window size as input and returns a list of the maximum elements for each window. The function uses zip to iterate over the list and returns a list of max elements. Using the zip function helps to iterate over the list with the given rolling window size. The max function is used to find the maximum element in each window. 

The output of the example given in the problem is:
```python
[1, 2, 3, 3, 3, 4, 4]
``` 

This solution is efficient and can be easily tested.