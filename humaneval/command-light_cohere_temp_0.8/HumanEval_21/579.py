```python
from typing import List

def rescale_to_unit(numbers: List[float]):
    # Apply linear transform to numbers list
    numbers_res = [x / (x + 1) for x in numbers]
    return numbers_res

# Test cases
numbers = [1.0, 2.0, 3.0, 4.0, 5.0]
result = rescale_to_unit(numbers)
```

This code defines a function named rescale_to_unit that takes a list of numbers as input and returns a new list where each element has been scaled up or down by a linear function that focuses on the difference between that element and the previous element. The function then passes this test cases to the function and it should return the expected output.