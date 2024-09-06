```python
from typing import List

def rescale_to_unit(numbers: List[float]) -> List[float]:
    return [(x-min(numbers))/(max(numbers)-min(numbers))*1 for x in numbers]
```

The function `rescale_to_unit` takes a list of numbers as input and returns a list of numbers scaled to the range [0, 1] based on the smallest and largest values in the input list. It computes the minimum and maximum values of the input list outside the main list comprehension and applies the transformation in the main list comprehension.

This approach ensures that the output list has the same length as the input list, with each element scaled appropriately based on the overall range of values in the input list.

Here is a sample output:
```python
rescale_to_unit([1.0, 2.0, 3.0, 4.0, 5.0])
[0.0, 0.25, 0.5, 0.75, 1.0]
```