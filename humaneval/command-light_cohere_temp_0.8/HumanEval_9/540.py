```python
from typing import List

def rolling_max(numbers: List[int]) -> List[int]:
    """ 
    From a given list of integers, generates a list of rolling 
    maximum elements found until a given moment in the sequence.
    """
    list of rolling maximum elements is returned 
    """
    numbers.sort()  # ascending order of numbers 
    rolling_max = []
    while True: 
        temp_max = numbers[-1]
        for num in numbers[:-1]: 
            if num > temp_max: 
                temp_max = num 
        rolling_max.append(temp_max)
        break 
    return rolling_max

# Example
numbers = [1, 2, 3, 2, 3, 4, 2]
rolling_max_example = rolling_max(numbers)
print(rolling_max_example)
``` 
This Python code defines a function called rolling_max that calculates and returns a list of rolling maximum elements in a given list of integers. The function first sorts the process to get a sorted ascending list of numbers. It then enters a process where it iterates through the sorted list, continually selecting the maximum element seen so far and adding it to the rolling_max list. The function returns the array of the rolling maximum elements.