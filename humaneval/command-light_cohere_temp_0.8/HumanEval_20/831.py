Here's the solution:
```python
from typing import List

def find_closest_elements(numbers: List[float]):
    """
    Returns a tuple containing the two closest elements in the list, along with their relative order.
    """
    list comparison with a tuple of values.
    num1 = min(numbers)
    arr = [num]
    for i in range(len(numbers)):
        if numbers[i] < num:
            num = numbers[i]
            arr.append(num)
    num2 = max(numbers)
            arr.append(num2)
    return arr
```
The function takes a list of float numbers as input and returns a tuple containing the two closest elements in the list, along with their relative order.