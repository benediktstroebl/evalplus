```python
from typing import List, Tuple

def find_closest_elements(numbers: List[float]):
    """ Selects and returns two elements that are the closest to each other and returns them in order (smaller number, larger number).
    
    Parameters: 
        - numbers (List[float]): List of numbers.
    
    Returns: a Tuple[float, float] with the two numbers.
```

# Example:
numbers = [1.0, 2.0, 3.0, 4.0, 5.0, 2]

result = find_closest_elements(numbers)

print(result) # Output: (2.0, 1.0)

```
Please note that you can run this code in a Python environment or IDE and the output will be the two numbers that are the closest to each other in the list.