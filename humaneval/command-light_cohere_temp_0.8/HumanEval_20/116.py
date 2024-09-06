```python
from typing import List

def find_closest_elements(numbers: List[float]):
    # Select two closest numbers
    x, y = min(numbers), max(numbers) - 1
    # Return tuple of two closest numbers in order (smaller, larger)
    return (x, y)

# Example of usage:
numbers = [1.0, 2.0, 3.0, 4.0, 5.0, 2]

result = find_closest_elements(numbers)
```