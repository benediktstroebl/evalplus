Here's the self-contained Python function that solves the problem of sorting numbers in markdown code blocks:
```python
from typing import List
def sort_numbers(lst_list: List[int]) -> List[int]:
    return [num for num in lst_list if num >= 0] + [num for num in lst_list if num > 0]
# Unit tests:
def test_sort_numbers():
    numbers = ["three", "one", "five", "six", "eight", "nine"]
    expected = [1, 3, 5, 6, 8, 9]
    result = sort_numbers(numbers)
    assert result == expected, "Sorted numbers don't match expected order."
```

This function takes a list of numbers and returns a new list with the positive numbers from the original list. It uses a necessary list comprehension to filter out the negative numbers. The result is then a new list with the positive numbers from the original list. 

The unit tests verify that the function's output matches the expected order of the numbers. It does this by comparing the result and expected values.