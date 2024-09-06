Here is a self-contained Python script that solves the problem:

```python
from typing import List

def rescale_to_unit(numbers: List[float]):
    # Apply a linear transform to the input list
    numbers_rescale = [num / max(numbers) for num in numbers]
    return numbers_rescale
```

This function takes a list of numbers as input and returns a new list where each value has been rescaled to the unit range [0, 1]. The function uses the max() function to find the maximum value in the input list, and then divides each number in the list by this maximum value to rescale it to the unit range.