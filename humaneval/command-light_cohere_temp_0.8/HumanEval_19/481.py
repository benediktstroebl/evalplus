Here is a Python script that contains a self-contained function that sorts and returns a list of numbers in ascending order:
```python
from typing import List

def sort_numbers(numbers: List[int]) -> List[int]:
    """
    Sorts the list of numbers.
    :param numbers: list of integers
    :return sorted list of integers
    """
    return sorted(numbers)

def test_sort_numbers():
    """
    Test the sort_numbers function with different lists of numbers
    """
    # Test case 1
    numbers = [1, 2, 3, 4, 5]
    expected = [1, 2, 3, 4, 5]
    got = sort_numbers(numbers)
    assert got == expected

    # Test case 2
    numbers = [5, 4, 3, 2, 1]
    expected = [1, 2, 3, 4, 5]
    got = sort_numbers(numbers)
    assert got == expected

    # Test case 3
    numbers = ['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
    expected = ['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
    got = sort_numbers(numbers)
    assert got == expected

# Run the test suite
test_sort_numbers()
``` 
This script defines a function sort_numbers that sorts a list of integers, as well as a test suite to ensure the correctness of the function. 

Please note that the code is designed to be self-contained, meaning it can be copied and pasted into another file without needing to reference external code or modules.