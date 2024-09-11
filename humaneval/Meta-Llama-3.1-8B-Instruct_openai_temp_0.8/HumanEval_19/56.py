### Sorting Numbers in a String
#### Problem Statement

Given a space-delimited string of numbers from 'zero' to 'nine', return the string with numbers sorted from smallest to largest.

#### Solution

```python
from typing import List

def sort_numbers(numbers: str) -> str:
    """
    Sorts numbers in a string from smallest to largest.

    Args:
    numbers (str): A space-delimited string of numbers from 'zero' to 'nine'.

    Returns:
    str: The sorted string.

    Example:
    >>> sort_numbers('three one five')
    'one three five'
    """
    
    # Split the input string into a list of numbers
    numbers_list: List[str] = numbers.split()

    # Define a dictionary to map numbers to their integer values
    number_map: dict[str, int] = {
        'zero': 0, 'one': 1, 'two': 2, 'three': 3, 'four': 4,
        'five': 5,'six': 6,'seven': 7, 'eight': 8, 'nine': 9
    }

    # Use a lambda function as the key for sorting, which returns the integer value of each number
    numbers_list.sort(key=lambda x: number_map[x])

    # Join the sorted list back into a string
    sorted_numbers: str =''.join(numbers_list)

    return sorted_numbers
```

#### Example Usage

```python
print(sort_numbers('three one five'))  # Output: 'one three five'
print(sort_numbers('nine four two'))   # Output: 'two four nine'
```