```python
from typing import List


def rescale_to_unit(numbers: List[float]):
    # Apply the linear transform to the input numbers
    numbers = [num / min(numbers) for num in numbers]
    return [1.0 if num < 0 else num for num in numbers]
```
This code implements a function called `rescale_to_unit` that takes a list of numbers and returns a new list with numbers scaled to the range [0, 1]. The function uses the `min` function to calculate the minimum value in the list, then divides each number by this minimum to ensure it's within the desired range.