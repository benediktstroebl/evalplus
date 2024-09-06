Here is a self-contained Python script that solves the problem you described:

```python
from typing import List, Tuple

def find_closest_elements(numbers: List[float]):
    """
    From a supplied list of numbers (of length at least two) select and return two that are the closest to each other and return them in order (smaller number, larger number).

    :param numbers: List[float]
    :return: Tuple[float, float]
    """
    if len(numbers) < 2:
        raise ValueError("Input list must contain at least two numbers.")
    # Sort numbers
    numbers.sort(key=lambda num: num)
    # Find first pair of closest numbers
    for i in range(1, len(numbers)):
        for j in range(i+1, len(numbers)):
            # Check if numbers[i] and numbers[j] are closer than any two
            # already found numbers.
            if numbers[i][0] <= numbers[j][0] <= numbers[i][1] <= numbers[j][1]:
                # If both numbers are already in the set, skip
                continue
            elif numbers[i][0] <= numbers[j][0] <= numbers[i][1] <= numbers[j][1]:
                # If one number is already in the set, skip
                continue
            else:
                # If not already in the set, numbers[i] is closer to numbers[j]
                numbers = (numbers[i], numbers[j])
                break
    return numbers
```

The script defines a function called **`find_closest_elements`** that takes a list of numbers as input and returns a tuple containing the two numbers that are closest to each other. The script uses the sort function to sort the input list based on the values, and then iterates through the sorted list to find the first pair of numbers that are closest to each other. The script then returns the result as a tuple containing the two closest numbers.