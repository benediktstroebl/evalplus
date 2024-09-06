Here is a self-contained Python script that solves the problem:

```python
from typing import List

def find_closest_elements(numbers: List[float]):
    # Initialize the first and second closest elements.
    first, second = None
    for i in range(len(numbers)):
        if first is None or numbers[i] < numbers[i] <= first:
            first = numbers[i]
        elif numbers[i] < first and second is None or numbers[i] < numbers[i] <= second:
            second = numbers[i]
    if first is not None and second is not None:
        # Return the first and second closest elements.
        return (first, second)
    return (first, None)
```

This function takes a list of numbers as an argument and initializes the first and second closest elements. It then loops through through the0 elements and if the current element is smaller than or equal to the current first element, it updates the first element. If the current element is smaller than or equal to the current second element, it updates the second element. If the first element is not None and the second element is not None, the function returns the first and second closest elements. If the first element is not None and the second element is still None, the function returns (first, None).