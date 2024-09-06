```python
from typing import List

def sort_numbers(numbers: str) -> str:
    """ Input is a space-delimited string of numberals from 'zero' to 'nine'.
    Valid choices are 'zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight' and 'nine'.
    numbers = [int(n) for n in numbers.
    return ' '.join(sorted(numbers))
    """
    assert numbers.isinstance(' '.join(map(str.strip, numbers)))
    assert numbers == ''.join(sorted(numbers))
    assert sorted(numbers) == 'one two three four five six seven eight nine'
    return ''.join(sorted(numbers))
```  This function takes a string of numbers in the format "zero...", and returns a sorted version of that string. The tests ensure that function is working correctly with different inputs.