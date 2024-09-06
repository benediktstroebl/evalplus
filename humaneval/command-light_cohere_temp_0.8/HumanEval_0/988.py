Here is a self-contained Python script that defines a function to check if any two numbers in a list are closer than a given threshold:

```python
from typing import List


def has_close_elements(numbers: List[float], threshold: float) -> bool:
    # sort numbers
    numbers.sort()

    # check
    close two numbers in list
    for i in range(len(numbers) - 1):
        if numbers[i] + numbers[i + 1] <= threshold:
            return True
    return False


# Example 
numbers = [1.0, 2.0, 3.0, 4.0, 5.0]
threshold = 0.3)
has_close_elements(numbers, 0.3)  # return True
```

This script defines a function called has_close_elements that takes in two parameters: a list of numbers and a threshold value. The function then sorts the list of numbers and then checks if any two numbers in the list are closer than the given threshold. The function returns True if any two numbers in the list are closer than the given threshold, and returns False otherwise. The example at the end demonstrates how the function can be used to solve the problem.