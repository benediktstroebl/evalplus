Here's a Python script that contains a function called has_close_elements, which takes a list of numbers and a threshold as input and returns a boolean indicating whether any two numbers in the list are closer to each other than the threshold. The function works correctly and passes the given tests. The code is formatted as a Markdown code block:
```python
from typing import List

def has_close_elements(numbers: List[float], threshold: float) -> bool:
    """
    Check if in given list of numbers, are any two numbers closer to each other than
    given threshold.
    """
    numbers.sort()
    for i in range(len(numbers) - 1):
        if numbers[i + 1] - numbers[i] < threshold:
            return True
    return False

# Tests
assert not has_close_elements([1.0, 2.0, 3.0], 0.5)
assert has_close_elements([1.0, 2.8, 3.0, 4.0, 5.0, 2.0], 0.3)
```

The function first sorts the input list of numbers. Then, it iterates through the list, and for each element, it checks if the next element is closer than the threshold to the current element. If there is a pair of numbers that are closer together than the threshold, the function returns True, otherwise, it returns False. 

The above code includes a testing example that demonstrates the functionality of the `has_close_elements` function with sample inputs. The test cases confirm that the function returns the expected outputs for the given inputs.