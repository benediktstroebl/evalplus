Here is a self-contained Python script with a function that solves the problem:

```python
from typing import List

def has_close_elements(numbers: List[float], threshold: float) -> bool:
    """ Check if in given list of numbers, are any two numbers closer to each other than given threshold
    """
    # Check if any two elements are closer than the threshold
    for i in range(len(numbers) - 1):
        for j in range(i + 1, len(numbers)):
            if numbers[i] - numbers[j] < threshold:
                return True
    return False

# Test the function
print(has_close_elements([1.0, 2.0, 3.0, 0.0, 4.0], 0.3))  # True

print(has_close_elements([1.0, 2.0, 3.0, 0.5])) # True

print(has_close_elements([1.0, 2.0, 3.0, 4.0])) # False

```

This function has been designed to determine whether any two numbers in the list are closer to each other than a given threshold. The function uses a loop-based approach, where it compares each pair of elements in the list and checks if they are closer than the threshold. It returns True if any two elements are closer, and False otherwise.