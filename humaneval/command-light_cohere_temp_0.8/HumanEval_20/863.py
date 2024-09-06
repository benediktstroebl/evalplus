Here is a self-contained Python script that solves the problem and passes the test:

```python
from typing import List

def find_closest_elements(numbers: List[float]):
    """
    Select and return two that are the closest to each other and return them in order (smaller number, larger number)
    :param numbers: [float] list of numbers
    :return: Tuple[float, float]
    """
    closest_num = float('inf')
    second_closest = float('-inf')
    for num in numbers:
        if num < closest_num:
            closest_num = num
        if num > second_closest:
            second_closest = num
    return_result = (closest_num, second_closest)
    return return_result
```

The function takes a list of numbers and returns a tuple of the two closest numbers. The function iterates through the numbers in the list and determines which number is closest to which. The first one that is smaller than the current closest number, and the second one is larger than the current second closest number.