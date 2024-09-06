```python
from typing import List

def rolling_max(numbers: List[int]) -> List[int]:
    """
    Generate a list of rolling maximum elements from the input list.
    """
    def rolling_max(numbers):
        max_num = numbers[0]
        max_index = 0
        result = [max_num]
        for num in numbers[1:]:
            if num > max_num:
                max_num = num
                max_index = index
            result.append(max_num)
        return result
    """

    test_numbers = [1, 2, 3, 2, 3, 4, 2]
    test_result = rolling_max(test_numbers)
    assert all([num == test_result[index] for index, num in enumerate(test_numbers)])
    assert all([num == test_result[-1] for num in test_numbers])

# Example of list of numbers to test the function
numbers = [1, 2, 3, 4, 5]
result = rolling_max(numbers)
assert all([num == result[index] for index, num in enumerate(numbers)])
``` 
This Python script defines a function called `rolling_max` that takes a list of integers as input and generates a new list of the rolling maximum elements. The `rolling_max` function uses a loop to compare each element in the input list with the current maximum element and updates the maximum value and its index accordingly. The function then returns the list of rolling maximum elements. 

The script also includes a set of test numbers and passes them through the `rolling_max` function to ensure that the function works correctly. The script then tests the values of the test numbers to make sure that the `rolling_max` function returns the correct results.