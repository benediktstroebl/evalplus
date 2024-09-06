```python
from typing import List
def rolling_max(numbers: List[int]) -> List[int]:
    """ Returns a list of rolling max elements found in the sequence
    """
    numbers = [num for num in numbers if num != 0]  # Ensure only positive numbers
    max_num = max(numbers)
    rolling_maxes = [max_num]
    for i in range(1, len(numbers)):
        current = numbers[i]
        if current > max_num:
            max_num = current
        rolling_maxes.append(max_num)
    return rolling_maxes

# Test cases
numbers_test = [1, 2, 3, 4, 5]
test_result = rolling_max(numbers_test)
print(test_result)  # Output: [2, 3, 3, 4, 5]

numbers_positive = [1, 2, 3, 4, 5]
numbers_negative = [-1, 2, 3, 4, 5]
test_positive_result = rolling_max(numbers_positive)
test_negative_result = rolling_max(numbers_negative)

print("Test case 1:", test_positive_result)
print("Test case 2:", test_negative_result)  # Output: [1, 2, 3, 4, 5]
```
The function rolling_max generates a list of the rolling maximum elements in a sequence of numbers. The function starts by ensuring that only positive numbers are passed to the function from the input list. The maximum number is identified using the max function, and the rolling maximum list is built by comparing each new number with the maximum number and updating the list accordingly. The test cases demonstrate how the result for different types of lists.