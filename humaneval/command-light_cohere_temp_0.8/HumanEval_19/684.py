```python
from typing import List

def sort_numbers(numbers: str) -> str:
    """ Input is a space-delimited string of numberals from 'zero' to 'nine'.
    Valid choices are 'zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight' and 'nine'.
    numbers = [int(num) for num in numbers.
    return ' '.join(sorted(numbers))
    """

    numbers = [0, 2, 3, 6, 7, 8, 9]
    assert sort_numbers("three one five") == "one three five"
    assert sort_numbers("zero two three four") == "two three four"
    assert sort_numbers(" eight nine ") == "eight nine"
    assert sort_numbers("abc123") == "123"
    assert sort_numbers(" eleven twelve ") == " eleven twelve "
    assert sort_numbers(" ten one hundred ") == " ten one hundred "

    print("All tests passed!")
```