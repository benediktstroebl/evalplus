Here's the Python code:
```python
from typing import List, Tuple

def find_closest_elements(numbers: List[float]):
    # Take the first two elements in the list
    x1, y1 = numbers[0], numbers[1]
    # Calculate the difference between the two numbers
    dist = abs(x1 - y1)
    # Check if the current pair is the smallest pair
    if dist < (numbers[2] - numbers[0]))[dist]:
        return (x1, y1)
    else:
        return (numbers[2], numbers[1])

# Example usage:
numbers = [1.0, 2.0, 3.0, 4.0, 5.0]
print_closest_elements(numbers)
```

This script defines a function called **`find_closest_elements`** that accepts a list of numbers as an argument. It then uses the first two elements in the list and calculates the difference between them. If this difference is smaller than the difference between the third and fourth elements, it means the first two elements are the closest. The function returns the two elements and returns them in order (smaller number, larger number).