```python
from typing import List

def has_close_elements(numbers: List[float], threshold: float) -> bool:
    """ Check if in given list of numbers, are any two numbers closer to each other than
    given threshold
    """
    for i in range(len(numbers) - 1):
        for j in range(i + 1, len(numbers)):
            if abs(numbers[i]-numbers[j]) < threshold:
                return True
    return False

# Test
numbers=[1.0, 2.0, 3.0, 0.0, 5.0, 2.0]
has_close_elements(numbers, 0.0) # False

# Test 2
numbers=[1.0, 2.0, 3.0, 0.0, 4.0]
has_close_elements(numbers, 0.0) # False

# Test 3
numbers=[1.0, 2.0, 3.0, 0.0, 5.0]
has_close_elements(numbers, 0.0) # False

# Test 4
numbers=[1.0, 1.0, 2.0, 3.0, 4.0]
has_close_elements(numbers, 0.0) # True

# Test 5
numbers=[1.0, 2.0, 3.0, 0.0, 3.0]
has_close_elements(numbers, 0.0) # False

# Test 6
numbers=[1.0, 2.0, 3.0, 0.0, 0.0]
has_close_elements(numbers, 0.0) # False

# Test 7
numbers=[1.0, 2.0, 3.0, 4.0, 5.0]
has_close_elements(numbers, 0.0) # True

# Test 8
numbers = [1.0, 2.0, 1.0, 0.0, 0.0, 3.0]
has_close_elements(numbers, 0.0) # False

print("Result:", has_close_elements(numbers, 0.0))