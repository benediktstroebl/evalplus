### Sorting Numbers in a String
#### Problem Description

Input is a space-delimited string of numberals from 'zero' to 'nine'. Valid choices are 'zero', 'one', 'two', 'three', 'four', 'five','six','seven', 'eight' and 'nine'. Return the string with numbers sorted from smallest to largest.

#### Solution
```python
from typing import Callable

# Dictionary to map string numbers to their integer values
number_map: dict[str, int] = {
    'zero': 0, 'one': 1, 'two': 2, 'three': 3, 'four': 4,
    'five': 5,'six': 6,'seven': 7, 'eight': 8, 'nine': 9
}

def sort_numbers(numbers: str) -> str:
    """
    Input is a space-delimited string of numbers from 'zero' to 'nine'.
    Valid choices are 'zero', 'one', 'two', 'three', 'four', 'five','six','seven', 'eight' and 'nine'.
    Return the string with numbers sorted from smallest to largest
    
    Args:
        numbers (str): A space-delimited string of numbers.
    
    Returns:
        str: The string with numbers sorted from smallest to largest.
    
    Example:
        >>> sort_numbers('three one five')
        'one three five'
    """
    # Split the input string into a list of numbers
    num_list: list[str] = numbers.split()

    # Sort the list of numbers based on their integer values
    sorted_num_list: list[str] = sorted(num_list, key=lambda x: number_map[x])

    # Join the sorted list back into a string
    sorted_numbers: str =''.join(sorted_num_list)

    return sorted_numbers
```

#### Example Use Cases
```python
print(sort_numbers('three one five'))  # Output: 'one three five'
print(sort_numbers('seven six five'))  # Output: 'five six seven'
print(sort_numbers('nine eight seven'))  # Output:'seven eight nine'
```