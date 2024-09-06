```python
from typing import List
def rescale_to_unit(numbers: List[float]):
    # Apply the linear transformation
    return [x / min(numbers) if min(numbers) != 0 else 1.0 for x in numbers]

# Test the function with some examples
numbers_list = [1.0, 2.0, 3.0, 4.0, 5.0]
rescale_to_unit(numbers_list)
# [0.0, 0.0, 0.0, 0]
[0.9, 1.0, 1.0, 0]
[0.0, 0, 0, 1.0]
# [1.0, 2.0, 3.0, 4]
[0.9, 0, 0, 1.0]
print(numbers_list)
```