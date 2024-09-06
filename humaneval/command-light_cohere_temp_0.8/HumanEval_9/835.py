```python
from typing import List

def rolling_max(numbers: List[int]) -> List[int]:
    """
    Returns the list of rolling max elements from the input list.
    """
    def rolling_max(numbers):
        # Initialize the result list with the first number
        rolling_maxes = [numbers[0]]

        # Loop through the list and add the next number to the result list if it's greater than the current rolling max
        for num in numbers[1:]:
            if num > rolling_maxes[-1]:
                rolling_maxes.append(num)
       [-1]
        return rolling_maxes
    """

# Test cases
numbers1 = [1, 2, 3, 4, 5]
print("Test case 1 result:", rolling_max(numbers1))

numbers2 = [6, 2, 4, 3, 5, 1]
print("Test case 2 result:", rolling_max(numbers2))

numbers3 = [1, 10, 9, 8, 7, 6, 5, 4, 3, 2]
print("Test case 3 result:", rolling_max(numbers3))

numbers4 = [10, 20, 15, 25, 10, 30, 5, 8, 3]
print("Test case 4 result:", rolling_max(numbers4))

```
This Python script defines a function called rolling_max, which generates a list of the rolling maximum elements from a given list of integers. The function uses a technique of "rolling max" to keep track of the maximum element as it moves through the list. 

The function is then tested with four different input lists, and the results are printed out.