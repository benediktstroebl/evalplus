```python
from typing import List

def rescale_to_unit(numbers: List[float]) -> List[float]:
    return [(x-min(numbers))/(max(numbers)-min(numbers)) * 1 for x in numbers]
```

The function `rescale_to_unit` takes a list of numbers as input and returns a list of numbers scaled to the range [0, 1] based on the smallest and largest values in the input list. You can use the function by calling it and passing in a list of numbers as demonstrated in the docstring. The returned list of numbers will be calculated based on the relative proportions of the values in the input list.