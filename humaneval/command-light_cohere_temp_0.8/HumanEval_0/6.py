```python
from typing import List

def has_close_elements(numbers: List[float], threshold: float) -> bool:
    """ Check if in given list of numbers, are any two numbers closer to each other than
    given threshold
    :return False if any(abs(x - y) > threshold for x, y in numbers) else True
    """
    return False if any(abs(x - y) > threshold for x, y in numbers) else True

# Unit tests
def test_has_close_elements():
    numbers = [1.0, 2.0, 3.0, 0.8, 4.0, 5.0, 6.0, 2.0, 0.0, 4, 6, 7.8, 9, 9.10, 12, 13, 14, 15, 16, 17, 18, 19, 20]
    for x, y in zip(numbers, numbers):
        if has_close_elements(numbers, 1.0):
            print("Passed test")
        else:
            print("Failed test")
    test_has_close_elements()

```
This code defines a function called has_close_elements that takes in a list of numbers and a threshold as input and returns a boolean indicating whether any two numbers in the list are closer than the threshold. The function checks if any two elements in the list are within the threshold of each other using the abs() function, and returns False if any of the conditions are met. The test function then creates a list of numbers and runs the function with it, and then prints a message indicating whether the test passed or failed based on the output of the function.