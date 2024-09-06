```python
from typing import List

def rescale_to_unit(numbers: List[float]) -> List[float]:
    return [(x-min(numbers))/(max(numbers)-min(numbers))*1 for x in numbers]
```

The function `rescale_to_unit` takes a list of numbers as input and returns a transformed list such that the smallest number in the input list becomes 0, and the largest number becomes 1. The transformation is a linear scaling based on the difference between the largest and smallest values in the input list. The function uses the `min` and `max` built-in functions to find the smallest and largest values respectively and applies the transformation formula `((x-min)/(max-min))*1` to each number in the list to get the desired scaling.

To validate the functionality of the function, let's test it with an example where the input list is `[1.0, 2.0, 3.0, 4.0, 5.0]`:
```python
print(rescale_to_unit([1.0, 2.0, 3.0, 4.0, 5.0]))
```

The output will be:
```
[0.0, 0.25, 0.5, 0.75, 1.0]
```

The function has also successfully transformed the input list `[1.0, 2.0, 3.0, 4.0, 5.0]` such that the smallest number (1.0) becomes 0 and the largest number (5.0) becomes 1.

This validation demonstrates that the function `rescale_to_unit` works as expected and provides a reliable tool to transform lists of numbers to a specific range.