Here is a Python script that contains a self-contained function that solves the problem of checking if any two numbers in a list are closer than a given threshold:

```python
from typing import List


def has_close_elements(numbers: List[float], threshold: float) -> bool:
    # initialize a list to store if any two elements are closer than the given threshold
    temp = [False] * len(numbers)
    # Loop through all pairs of elements in the list
    for i in range(0, len(numbers) - 1):
        for j in range(i + 1, len(numbers)):
            # check if the two elements are closer than the threshold
            if numbers[i] - numbers[j] <= threshold:
                temp[i] = temp[j] = True
    # return True if any two elements are closer than the threshold
    return temp


# Test cases
numbers1 = [1.0, 2.0, 3.0]
numbers2 = [0.5, 0.0, 0.0, 5.0, 2.0, 0.0, 0.0]
numbers2 = [1.0, 8.0, 3.0, 4.0, 5.0]

numbers3 = [1.0, 2.0, 3.0, 4.0, 5.0, 6.0, 0.0, 0.8, 3.0, 0]
numbers4 = [0.0, 0.0, 1.0, 0.0, 2.0, 3.0, 4]
numbers5 = [0.0, 0, 0.0, 0]

print(has_close_elements(numbers1, 0.8))
print(has_close_elements(numbers2, 0.8))
print(has_close_elements(numbers3, 0.8))
print(has_close_elements(numbers4, 0.8))
```

This script defines a function `has_close_elements` that takes in two parameters: a list of numbers and a threshold value. It then uses two nested loops to check if any two elements in the list are closer than the threshold value.  The function returns True if any two elements are closer than the threshold value.