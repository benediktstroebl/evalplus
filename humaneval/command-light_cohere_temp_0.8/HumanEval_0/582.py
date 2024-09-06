```python
from typing import List

def has_close_elements(numbers: List[float], threshold: float) -> bool:
    """
    Check if in the list of numbers, are any two numbers closer to each other than the given threshold
    """
    for i in range(len(numbers) - 1):
        for j in range(i + 1, len(numbers)):
            if numbers[i] - numbers[j] < threshold:
                return True
    return False

# Test
print(has_close_elements([1.0, 2.0, 3.0], 0.1)) # True

print(has_close_elements([1.0, 2.0, 3.0], 0.1)) # False

print(has_close_elements([1.0, 2.8, 3.0], 0.2)) # True

print(has_close_elements([1.0, 2.8, 3.0], 0.2)) # True

print(has_close_elements([1.0, 2.0, 3.0], 0.3)) # False

print(has_close_elements([1.0, 3.0, 2.0], 0.4)) # True)

print(has_close_elements([1.0, 2.0, 3.0], 0.5)) # False)

print(has_close_elements([1.0, 2.0, 3.0], 0.6)) # False)

print(has_close_elements([1.0, 2.0, 3.0], 0.7)) # True)

print(has_close_elements([1.0, 3.0, 2.0], 0.8)) # False)

print(has_close_elements([1.0, 2.0, 3.0], 0.9)) # False)

print(has_close_elements([1.0, 1.0, 2.0], 0.10)) # False)

``` 
This script defines a function called has_close_elements that takes a list of numbers and a threshold as input and returns a boolean value indicating whether any two elements in the list are closer than the threshold. 

The script then tests the function with a variety of inputs and prints the results. 

The function uses two for loops to compare each element in the list to every other, and returns True if any two elements are closer than the threshold. 

Note: the code is a self-contained Python function that checks if a list of numbers contains any pair of numbers that are closer to each other than a threshold.