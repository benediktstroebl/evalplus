Here is a self-contained Python script that solves the problem of sorting numbers in Markdown code blocks:
```python
from typing import List
def sort_numbers(lst: List[int]) -> List[int]:
    """ Input is a list of integers.
    Numbers are sorted in ascending order
    """
    return sorted(lst)

# Example usage:
numbers = [3, 1, 5]
sorted_numbers = sort_numbers(numbers)
print("Sorted numbers:", sorted_numbers)  # Output: [1, 3, 5]
```
This script defines a function sort_numbers that takes a list of integers as input and returns a sorted list of integers. The function utilizes the Python's built-in sorted() function to arrange the numbers in ascending order. The output of the function call is displayed on the console.