Here is a self-contained Python script with a function that sorts a list of numbers in a markdown code block:
```python
from typing import List


def sort_numbers(numbers: List[int]) -> List[int]:
    """ Input is a list of numbers, returns a sorted list"""
    return sorted(numbers)

# Example list to be sorted
test_list = [3, 1, 5]

# Function call
sorted_test = sort_numbers(test_list)
print("Sorted numbers:", sorted_test)
``` 
The code defines a function called `sort_numbers` that takes a list of numbers as input and returns a new list, which is the sorted version of the input list. The function uses the `sorted` function from the built-in Python library to sort the numbers in ascending order.