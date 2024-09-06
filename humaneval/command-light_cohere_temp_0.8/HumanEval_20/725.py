```python
from typing import List

def find_closest_elements(numbers: List[float]):
    # Select two closest elements
    close1 = min(numbers[:-count(1)], numbers[:-count(0)])
    close2 = min(numbers[count(1) :], numbers[count(0) : count(1)])
    return close1, close2

# Test the function with a markdown code block
numbers = [1.0, 2.0, 3.0, 4.0, 2]
# Output: (1.0, 2.0)
```

This is the solution to the problem in a Python script. You can use this function to solve the problem and pass your markdown code block as an argument to the function.