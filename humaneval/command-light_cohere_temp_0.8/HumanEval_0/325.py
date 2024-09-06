```python
from typing import List

def has_close_elements(numbers: List[float], threshold: float) -> bool:
    """ Check if in given list of numbers, are any two numbers closer to each other than
    given threshold
    """
    # iterating through the list of numbers
    for i in range(len(numbers) - 1):
        for j in range(i + 1, len(numbers)):
            # check if the current number is closer to the next number than the threshold
            if numbers[i] <= numbers[j] + threshold:
                return True
    return False

# tests
print(has_close_elements([1.0, 2.0, 3.0], 0.1)) # True
5
print(has_close_elements([1.0, 2.8, 3.0], 0.2)) == False
0
print(has_close_elements([1.0, 2.0, 0.0], 0.5)) == True
0
print(has_close_elements([1.0, 2.0, 3.0], 0.5)) == False
0
print(has_close_elements([1.0, 2.8, 3.0], 0.6)) == False
0
print(has_close_elements([1.0, 2.0, 3.0], 0.1)) == True
0
print(has_close_elements([1.0, 2.0, 3.0], 1.5)) == True
0
print(has_close_elements([1.0, 2.0, 3.0], 2.5)) == False
0
print(has_close_elements([1.0, 2.0, 3.0], 4.5)) == False
0
print(has_close_elements([1.0, 2.0, 3.0], 5.5)) == False
0
print(has_close_elements([1.0, 2.0, 3.0], 6.5)) == False
0
print(has_close_elements([1.0, 2.0, 3.0], 7.5)) # <