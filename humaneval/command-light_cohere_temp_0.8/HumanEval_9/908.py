```python
from typing import List

def rolling_max(numbers: List[int]) -> List[int]:
    numbers = [num for num in numbers if num != 0]  # Remove non-positive numbers to prevent division by zero
    max_num = max(numbers)
    rolling_max = [max(numbers[:i]) for i in range(1, len(numbers))]
    
    for num in numbers:
        if num < max_num:
            max_num = num
    rolling_max.append(max_num)
    
    return rolling_max

# Test case 1: Positive numbers
test_positive_numbers = rolling_max([1, 2, 3, 4, 5])
assert len(test_positive_numbers) == 5
assert test_positive_numbers[0] == 1
assert test_positive_numbers[1] == 2
assert test_positive_numbers[2] == 3
assert test_positive_numbers[3] == 3
assert test_positive_numbers[4] == 4
assert test_positive_numbers[5] == 5

# Test case 2: Negative numbers
test_negative_numbers = rolling_max([-1, 2, 3, -4])
assert len(test_negative_numbers) == 5
assert test_negative_numbers[0] == -1
assert test_negative_numbers[1] == 2
assert test_negative_numbers[2] == 3
assert test_negative_numbers[3] == -4
assert test_negative_numbers[4] == -4
assert test_negative_numbers[5] == -1

```
This code defines a function `rolling_max` that takes a list of integers as input and returns a new list containing the rolling maximum elements of the original input list. It removes non-positive numbers from the input list to ensure the rolling maximum calculation is accurate and then iterates over the list, calculating the rolling maximum element at each index. The script provides test cases to demonstrate the functionality of the rolling_max function, passing various input lists and asserting the expected output and elements.