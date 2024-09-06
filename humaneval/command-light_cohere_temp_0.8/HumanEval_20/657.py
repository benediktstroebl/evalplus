```python
from typing import List

def find_closest_elements(numbers: List[float]):
    # Select the first and second smallest numbers in the list
    first, second = min(numbers[:-len(numbers)//2]), max(numbers[:len(numbers)//2]))
    # Return the two closest elements in the list
    return (first, second)

# Test
numbers = [1.0, 2.0, 3.0, 4.0, 5.0, 2]

result = find_closest_elements(numbers)

print(result) # Prints the closest two elements in the list
```