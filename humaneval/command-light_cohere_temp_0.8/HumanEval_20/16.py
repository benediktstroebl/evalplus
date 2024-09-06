Here's a Python script that contains a self-contained function that solves the problem:

```python
from typing import List, Tuple

def find_closest_elements(numbers: List[float]):
    """
    from typing import List
    from math import sqrt
    numbers.sort()
    worst = numbers[0]
    for i in range(1, len(numbers)):
        if numbers[i] < worst:
            worst = numbers[i]
    smallest = worst
    for i in range(len(numbers)):
        if numbers[i] < worst:
            worst = numbers[i]
            smallest = i
    return smallest, worst
```

The function takes a list of numbers and returns a tuple containing the two elements that are the closest to each other. The function first sorts the worst and then smallest. It then iterates through the starting from the last element in the list and comparing each element to worst. The function will then return the smallest element and the worst element in the tuple.