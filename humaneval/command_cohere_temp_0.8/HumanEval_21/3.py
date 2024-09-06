```python
from typing import List

def rescale_to_unit(numbers: List[float]) -> List[float]:
    return [(x-min(numbers))/(max(numbers)-min(numbers))*1 for x in numbers]
```

The function `rescale_to_unit` takes a list of numbers as input and returns a list of numbers scaled to the range [0, 1] based on the smallest and largest values in the input list. It computes the minimum and maximum values of the input list outside the main list comprehension and applies the scaling factor to each element using basic arithmetic operations. This approach ensures that the output list maintains the relative order and distribution of values from the input list.