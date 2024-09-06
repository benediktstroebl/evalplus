Here's a Python script that contains a function called `rolling_max` that takes a list of integers `numbers` as input and returns a list of rolling maximum elements found at any given moment in the sequence:
```python
from typing import List, Tuple

def rolling_max(numbers: List[int]) -> List[int]:
    rolling_maxes = [num for num in numbers]
    for i in range(1, len(numbers)):
        if numbers[i] > numbers[i - 1]:
            rolling_maxes[i] = numbers[i]
    return rolling_maxes
```

This script defines a function called `rolling_max` that takes a list of integers `numbers` as input and returns a list of the maximum elements encountered up to any given point in the sequence.

The function utilizes a list comprehension to initialize `rolling_maxes` with the values from the input `numbers` list. It then iterates through the list, comparing each element to its previous element, and updates `rolling_maxes` when a maximum is encountered.

This approach is efficient and avoids unnecessary complexity and extra variables, making it an optimal solution for the problem. 

You can verify the function's correctness by testing it with various input lists, such as `[1, 2, 3, 2, 3, 4, 2]`, which should return `[1, 2, 3, 3, 3, 4, 4]`.