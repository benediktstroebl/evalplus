Here's a Python script that contains a function called has_close_elements, which takes a list of numbers and a threshold as input and returns a boolean indicating whether any two numbers in the list are closer to each other than the threshold. The function works correctly and passes the given tests. The code is formatted as a markdown code block:
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
numbers_list_1 = [1.0, 2.0, 3.0]
threshold_1 = 0.5
test_1 = has_close_elements(numbers_list_1, threshold_1)
print(test_1) 

numbers_list_2 = [1.0, 2.8, 3.0, 4.0, 5.0, 2.0]
threshold_2 = 0.3
test_2 = has_close_elements(numbers_list_2, threshold_2)
print(test_2)
```

The first test case represents a list of numbers [1.0, 2.0, 3.0] and a threshold of 0.5, which returns False. The second test case represents a list of numbers [1.0, 2.8, 3.0, 4.0, 5.0, 2.0] and a threshold of 0.3, which returns True. The output of each test case is printed to show the function's behavior and confirm that it passes both tests.