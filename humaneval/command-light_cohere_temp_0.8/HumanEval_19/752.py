Here is a self-contained Python script that includes the function `sort_numbers` that sorts a list of numbers in ascending order:
```python
from typing import List
def sort_numbers(numbers: List[int]) -> List[int]:
    """
    Sorts a list of numbers in ascending order and returns the sorted list.
    >>> sort_numbers([3, 1, 5])
    [1, 3, 5]
    """
    return sorted(numbers)
def test_sort_numbers():
    numbers = [3, 1, 5]
    expected = [1, 3, 5]
    actual = sort_numbers(numbers)
    assert expected == actual
test_sort_numbers()
``` 
This script defines a function `sort_numbers` that takes a list of numbers and returns a new list with the numbers sorted in ascending order. 
It also defines a function `test_sort_numbers` that contains a test list and an expected outcome. The script then executes the test_sort_numbers() function, which contains the test list and the expected outcome. 

Finally, the code uses the `assert` statement to check if the actual outcome matches the expected outcome.