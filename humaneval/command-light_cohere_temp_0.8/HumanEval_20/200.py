```python
from typing import List, Tuple

def find_closest_elements(numbers: List[float]):
    # two closest elements in a list
    # Select the two closest elements in the list
    # then return them in order (smaller number, larger number)
    closest1, closest2 = sorted((numbers[0], numbers[1]), key=lambda x: x[0]), reverse=True)
    return closest1, closest2

# Test the function
numbers = [1.0, 2.0, 3.0, 4.0, 5.0, 2]

result = find_closest_elements(numbers)
print(result) # (2.0, 3.0)
```