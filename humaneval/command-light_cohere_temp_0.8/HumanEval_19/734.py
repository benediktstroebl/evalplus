```python
from typing import List
def sort_numbers(numbers: str) -> str:
    """ Input is a space-delimited string of numbers from zero to nine.
    Valid choices are strings only with numbers from zero to nine.
    Convert to a sorted list of integers
    """
    return ' '.join(sorted(int(x) for x in numbers.
    
def test_sort_numbers() -> None:
    """ Tests the sort_numbers function with various input strings."""
    test_case = """
    Input: three one five 
    Expected Output: one three five
    """
    assert sort_numbers(test_case) == 'one three five', "Error in sorting numbers."
```