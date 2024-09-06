```python
from typing import List, Tuple

def find_closest_elements(numbers: List[float]):
    # use sorted to get the two closest elements
    closest1 = float('inf')
    closest2 = float('-inf')
    for n in numbers:
        if n > closest1:
            closest1 = n
        elif n > closest2:
            closest2 = n
    # return the two closest numbers in order
    return Tuple(closest1, closest2)

# tests
test_numbers = [1.0, 2.0, 3.0, 4.0, 5.0, 6.0]
print_closest_elements(test_numbers)

print(test_numbers)  # [1.0, 2.0]
```