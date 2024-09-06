Here is the solution to the problem:

```python
from typing import List, Tuple

def find_closest_elements(numbers: List[float]):
    # Initialize variables
    min_val = float("inf")
    max_val = float("-inf")
    closest1 = float("inf")
    closest2 = float("-inf")
    num_count1 = 0
    num_count2 = 0
    for num in numbers:
        if num < min_val:
            min_val = num
        num_count1 += 1
        if num > max_val:
            max_val = num
        num_count2 += 1
        if num < closest1:
            closest1 = num
        if num > closest2:
            closest2 = num
    if num_count1 == 1 and num_count2 == 1:
        return (closest1, closest2)
    if num_count1 == 2 and num_count2 == 1:
        return (closest2, closest1)
    return (min_val, max_val)
```

This code defines a function called **`find_closest_elements`** that takes a list of numbers as input. It iterates through list of numbers and finds the two closest numbers to each other. It then returns a number one and two in that order.

The function uses the **`List`** and **`Tuple`** data types, as well as the **`float`** data type. It also uses the ** typings** to ensure that the function is well-typed and can be used with **`List`** and **`Tuple`** in Python 3 and later.