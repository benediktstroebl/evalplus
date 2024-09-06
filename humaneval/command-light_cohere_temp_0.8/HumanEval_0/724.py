```python
from typing import List

def has_close_elements(numbers: List[float], threshold: float) -> bool:
    """
    Check if in given list of numbers, are any two numbers closer to each other than
    the threshold
    """
    # Implement your logic here
    # For this problem, we'll use simple brute force and compare each pair of adjacent elements until we find a match or hit the threshold
    return any(abs(numbers[i] - numbers[i-1]) <= threshold for i in range(len(numbers)-1))
```