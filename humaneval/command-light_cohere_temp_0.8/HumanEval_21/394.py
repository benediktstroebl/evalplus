Here is a Python script with a self-contained function that solves the problem:

```python
def rescale_to_unit(numbers):
    #type: List[float]
    numbers.transformed = []
    list(map(lambda x: (1 + x) / 6.0, numbers)))
    return transformed
```

This function takes a list of numbers as an input and applies a linear transform to that list, such that the smallest number will become 0 and the largest will become 1. The function then returns a list of transformed numbers.

For example, if the input is [1.0, 2.0, 3.0, 4.0, 5.0], the5.0], the0.

In this case, the function would return [0.0, 0.0, 0.75, 1.0] as the it outputs a list of numbers in the specified order. 

This is a self-contained function, which means it does not require any additional inputs or outputs. It can be used as a block in a Python script, as shown below:

```python
from typing import List

def rescale_to_unit(numbers: List[float]):
    numbers.transformed = []
    list(map(lambda x: (1 + x) / 6.0, numbers)))
    return transformed

numbers = [1.0, 2.0, 3.0, 4.0, 5.0]
transformed = rescale_to_unit(numbers)

print(transformed)
```
This would print [0.0, 0.75, 1.0] as the. print.