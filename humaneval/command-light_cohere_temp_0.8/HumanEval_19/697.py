```python
from typing import List

def sort_numbers(numbers: str) -> str:
    """ Input is a space-delimited string of numberals from 'zero' to 'nine'.
    Valid choices are 'zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight' and 'nine'.
    return numbers.
    """ Convert each number in the string, must have one of the following:
    ```
     - Zero
    ```
     - One
    ```
     - Two
    ```
     - Three
    ```
     - Four
    ```
     - Five
    ```
     - Six
    ```
     - Seven
    ```
     - Eight
    ```
     - Nine
    """
    numbers = numbers.strip()
    lower()
    numbers = sorted(numbers)
    return numbers

# Tests
numbers = 'three one five'
print(sort_numbers(numbers))  # Output: 'one threefive'

numbers = 'zero one two three four five six seven eight nine'
print(sort_numbers(numbers))  # Output: 'zero nine eight seven six five four three one two'

numbers = 'zero two one three five six seven eight nine'
print(sort_numbers(numbers))  # Output: 'twoone nine eight seven six five four'

numbers = 'zerobyone'
print(sort_numbers(numbers))  # Error: Function expected string, not 'zerobyone'
```