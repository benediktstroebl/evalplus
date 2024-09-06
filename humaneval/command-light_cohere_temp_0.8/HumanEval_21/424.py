```python
from typing import List
def rescale_to_unit(numbers: List[float]):
    # Apply a linear transform to that list, such that the smallest number will become 0 and the largest will become 1
    numbers = [x / 100 for x in numbers]
    return numbers

# Test case 1
input_data = [1.0, 2.0, 3.0, 4.0, 5.0]
print(rescale_to_unit(input_data)) == [0.0, 0.0, 0.0, 0.0])
# Test case 2
input_data = [1.0, 2.0, 3.0, 4.0]
print(rescale_to_unit(input_data) == [0.0, 0.0, 0.0, 1.0])
# Test case 3
input_data = [10.0, 10.0, 1000.0, 10000.0]
print(rescale_to_unit(input_data) == [0.0, 0.0, 0.0, 1.0])
```