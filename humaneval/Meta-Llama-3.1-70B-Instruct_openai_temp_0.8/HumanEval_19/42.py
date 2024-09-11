```python
from typing import List

def sort_numbers(numbers: str) -> str:
    """
    Input is a space-delimited string of numberals from 'zero' to 'nine'.
    Valid choices are 'zero', 'one', 'two', 'three', 'four', 'five','six','seven', 'eight' and 'nine'.
    Return the string with numbers sorted from smallest to largest
    >>> sort_numbers('three one five')
    'one three five'
    """
    # Define a dictionary to map word numbers to their integer values
    num_dict = {
        'zero': 0, 'one': 1, 'two': 2, 'three': 3, 'four': 4,
        'five': 5,'six': 6,'seven': 7, 'eight': 8, 'nine': 9
    }

    # Split the input string into a list of words
    num_list: List[str] = numbers.split()

    # Sort the list of words based on their integer values
    sorted_list: List[str] = sorted(num_list, key=lambda x: num_dict[x])

    # Join the sorted list of words back into a string separated by spaces
    sorted_str: str =''.join(sorted_list)

    return sorted_str

# Example usage:
print(sort_numbers('three one five'))  # Outputs: 'one three five'
```

Alternatively, you could use the `enum` module to define an enumeration of word numbers, which would make the code more concise:

```python
from enum import Enum
from typing import List

class Number(Enum):
    zero = 0
    one = 1
    two = 2
    three = 3
    four = 4
    five = 5
    six = 6
    seven = 7
    eight = 8
    nine = 9

def sort_numbers(numbers: str) -> str:
    num_list: List[str] = numbers.split()
    sorted_list: List[str] = sorted(num_list, key=lambda x: Number[x].value)
    sorted_str: str =''.join(sorted_list)
    return sorted_str

# Example usage:
print(sort_numbers('three one five'))  # Outputs: 'one three five'
```