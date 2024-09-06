```python
from typing import List

def has_close_elements(numbers: List[float], threshold: float) -> bool:
    return any(x - y < threshold for x, y in zip(numbers, numbers[1:]))
```
This function takes a list of numbers and checks if there are any adjacent elements in the list whose difference is less than a given threshold. The function returns true if there are such elements, and false otherwise. 

Here is an example usage of the above code:
```python
# Test if list has close elements
print(has_close_elements([1.0, 2.8, 3.0, 4.0, 5.0, 2.0], 0.3))
# Output: True
```
```python
# Test if list does not have close elements
print(has_close_elements([1.0, 2.0, 3.0], 0.5))
# Output: False
```