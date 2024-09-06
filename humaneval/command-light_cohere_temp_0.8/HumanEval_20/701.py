```python
from typing import List, Tuple

def find_closest_elements(numbers: List[float]):
    """
    Selects two elements that are the closest to each other and returns them in order (smaller number, larger number)
    :param numbers: List of floats, length at least 2
    :return: Tuple of float, float
    """
    def compare(num1, num2):
        # a simple floating-point comparison
        return num1 < num2

    # sort numbers
    sorted_numbers = sorted(numbers, key=compare)

    # get two closest numbers
    num1 = sorted_numbers[0]
    num2 = sorted_numbers[1]

    return num1, num2
```

You can use this function with a list of floating-point numbers to find the closest pair of numbers in the list. This is an very simple, straightforward solution to the problem.