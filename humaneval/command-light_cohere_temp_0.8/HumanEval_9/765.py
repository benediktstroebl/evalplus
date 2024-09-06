Here is a self-contained Python script that defines a function `rolling_max` that generates a list of the rolling maximum elements in a given list of integers:
```python
from typing import List

def rolling_max(numbers: List[int]) -> List[int]:
    """
    Returns a list of rolling maximum elements found until a given moment in the sequence.
    Each element is the maximum value of the current element, 
    and the next element (rolling window) is used to update the maximum.
    """
    list of integers, such that the length of the list is greater than 1.
    """
    list of integers, such that the length of the list is greater than 1.
    # Initialize the first and second elements as the smallest and largest numbers in the list respectively.
    numbers = sorted(numbers)
    largest = numbers[0]
    smallest = numbers[0]
    for num in numbers[1:]:
        if num > largest:
            largest = num
        elif num < smallest:
            smallest = num
        else:
            break  # Stop the loop when max and min are the same
    # Update the rolling window with the current maximum value and the next element.
    return [ list(numbers[1:][:2:-1] + [largest, smallest]))
```

This function sorts the input list of integers, and then uses a loop to compare each element with both the current maximum value and the next element in the list. It keeps updating the also the smallest and largest values in the list, and at the same time maintains the rolling window.