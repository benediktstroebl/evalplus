Here is a Python script with a self-contained function that solves the problem:

```python
from typing import List


def has_close_elements(numbers: List[float], threshold: float) -> bool:
    # sort list of numbers
    numbers.sort()
   

    # remove any duplicate numbers, if they are greater than threshold
    for n, i in enumerate(numbers):
        if numbers[i] > threshold:
            numbers[i], numbers.remove(n, numbers)
    # check if any two numbers in the list are closer than threshold
    for i, j in enumerate(numbers):
        if i < j:
            a, b = numbers[i], numbers[j]
            if a + b < threshold:
                return True
    return False


# test
numbers = [1.0, 2.0, 3.0, 4.0, 5.0, 2.0]
numbers = sorted(numbers)
numbers.remove(numbers[3])
result = has_close_elements(numbers, 0.0)
print(result)
```

This script defines a function called `has_close_elements` that takes in a list of numbers and a threshold as input and returns a boolean indicating whether any two numbers in the list are closer than the threshold.  The function sorts the list of numbers, removes any duplicate numbers that are greater than the threshold, and then checks if any two numbers in the list are closer than the threshold. The function then returns a boolean value that indicates whether this condition is true.

Finally, it tests the function by passing a list of numbers to the function with a threshold of 0.0 and prints the result, which should return True.