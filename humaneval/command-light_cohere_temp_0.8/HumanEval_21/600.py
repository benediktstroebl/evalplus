```python
from typing import List

def rescale_to_unit(numbers: List[float]):
    # Apply the linear transform
    numbers = [x / 100.0 for x in numbers]
    return numbers

# Test the function with a set of numbers in markdown code block
test_data = [0.75, 0.0, 2.0, 4.0, 0.0]

# Pass all test cases and print the results
rescale_results = rescale_to_unit(test_data)
print(rescale_results)
```