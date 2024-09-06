```python
from typing import List

def find_closest_elements(numbers: List[float]):
    # Select two elements that are closest to each other
    x1, y1 = numbers[::sort()][0] + numbers[::sort()][1]
    x2, y2 = numbers[::sort()][1] + numbers[::sort()][0]
    return (x1, y1), (x2, y2)

# Test
numbers = [1.0, 2.0, 3.0, 4.0, 5.0, 2]

result = find_closest_elements(numbers)
print(result)
```