Here's the solution:

```python
from typing import List

def has_close_elements(numbers: List[float], threshold: float) -> bool:
    #define two lists
    compare = [a for a in numbers if a <= threshold]
    between = [a for a in numbers if a >= threshold]
    # Return True if between is empty
    return not between

# Test cases:
numbers = [1.0, 2.0, 3.0, 4.0, 5.0, 0.0, 8.0, 2, 0.0, 3]
threshold = 0.5

result = has_close_elements(numbers,threshold)
```