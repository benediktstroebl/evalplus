Here's a self-contained Python script that solves the problem you've described:
```python
from typing import List


def has_close_elements(numbers: List[float], threshold: float) -> bool:
    # Sort the input list of numbers
    numbers.sort(sorted(numbers, key=lambda x: x))
    # Find the smallest and largest elements in the list
    smallest = numbers[0]
    largest = numbers[-1]
    # Check if any two adjacent elements are closer than the threshold
    for i in range(1,len(numbers)-1):
        current = numbers[i]
        next = numbers[i+1]
        if abs(current - next) < threshold:
            return True
    return False

# Test the function
input_numbers = [1.0, 2.0, 3.0, 0.8, 4.0, 5.0]
result = has_close_elements(input_numbers, 0.0)  # Output is True
```
This script first sorts the input list of numbers, then checks if there are any two adjacent numbers that are closer than a given threshold. The function returns True if this condition is met, indicating that the input list has at least one pair of numbers that are close to each other.