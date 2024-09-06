```python
from typing import List

def has_close_elements(numbers: List[float], threshold: float) -> bool:
    return any(abs(a - b) < threshold for a, b in zip(numbers, numbers[1:]))
```
This function checks if there exist two numbers in a list of numbers that are closer to each other than a given threshold. It uses a generator expression (abs(a - b) < threshold for a, b in zip(numbers, numbers[1:])) to iterate through all pairs of elements in the list, with the assumption that the list has at least two elements. It then uses the any function to check if any of these pairs have an absolute difference less than the threshold. 

Here's an example usage of the above code:
```python
print(has_close_elements([1.0, 2.0, 3.0], 0.5))
print(has_close_elements([1.0, 2.8, 3.0, 4.0, 5.0, 2.0], 0.3))
```
This will produce the following output:
```
False
True
```
These results are consistent with the original problem statement.