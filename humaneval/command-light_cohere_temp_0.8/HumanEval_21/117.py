```python
from typing import List
def rescale_to_unit(numbers: List[float]):
    # Apply linear transformation to the numbers list, so that the smallest number becomes 0 and the largest becomes 1
    numbers = [num / max(numbers) for num, max in zip(numbers, numbers)]
    return numbers

# Test the function
test_numbers = [0.5,2.0,3.0,0.0,0.0, 0.5]

print(rescale_to_unit(test_numbers)) == [0.0, 0.0, 0.0, 0.0])
```