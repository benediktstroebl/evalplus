```python
from typing import List

def sort_numbers(numbers: str) -> str:
    """ Input is a space-delimited string of numberals from 'zero' to 'nine'.
    Valid choices are 'zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight' and 'nine'.
    numbers = [int(x) for x in numbers. Sort the list of numbers in ascending order.
    return ''.join(sorted(numbers))
    """
    pass

    test_data = {
        "Input": "three one five",
        "Expected Output": "one three five"
    }
    assert sort_numbers(test_data["Input"]) == test_data["Expected Output"]
    print("Test passed!")
```