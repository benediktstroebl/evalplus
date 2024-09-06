Here is a Python script that contains a self-contained function that solves the problem of finding the closest elements between two numbers in a list:

```python
from typing import List, Tuple

def find_closest_elements(numbers: List[float]):
    """ From a supplied list of numbers (of length at least two) select and return two that are the closest to each other and return them in order (smaller number, larger number).

    Parameters:
        numbers: List[float] - List of floating-point numbers.
    Returns:
        Tuple[float, float] - A tuple of the two closest numbers.

    """
    return numbers[ Tuple[float, float]]
    """

    # Sort the list of numbers
    numbers.sort(key=lambda x: -x)

    # Get the two closest numbers
    num1 = numbers[0]
    num2 = numbers[1]

    # Compare the two numbers
    while True:
        # If the current number is smaller than the previous number
        if num1 == num2:
            break
        # Increase the index of the smaller number
        num1_index = numbers.index(num1)
        # Decrease the index of the larger number
        num2_index = numbers.index(num2)
        # Move the larger number to the end of the list
        numbers[num2_index], num1] = numbers[num1_index], num2
        # Move the smaller number to the end of the list
        numbers[num1_index], num1] = num1, num2_index
        num1, num2 = num2, num1

    return num1, num2
```

This function takes a list of numbers as input and returns a tuple of the two closest numbers in the list, in order. The function first sorts the numbers list and then gets the two closest numbers. Then the function compares the time by comparing the two numbers and moving the smaller number to the right of the larger number in the list. Finally, the function returns the two numbers as the closest pair.