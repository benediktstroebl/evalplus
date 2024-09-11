```python
from typing import List

def sort_numbers(numbers: str) -> str:
    """
    Input is a space-delimited string of numberals from 'zero' to 'nine'.
    Valid choices are 'zero', 'one', 'two', 'three', 'four', 'five','six','seven', 'eight' and 'nine'.
    Return the string with numbers sorted from smallest to largest
    """
    # Define a dictionary to map numberals to their integer values
    numeral_map = {
        'zero': 0, 'one': 1, 'two': 2, 'three': 3, 'four': 4,
        'five': 5,'six': 6,'seven': 7, 'eight': 8, 'nine': 9
    }

    # Split the input string into a list of numberals
    numeral_list: List[str] = numbers.split()

    # Sort the list of numberals based on their integer values
    sorted_numerals = sorted(numeral_list, key=lambda x: numeral_map[x])

    # Join the sorted list of numberals back into a string
    sorted_string =''.join(sorted_numerals)

    return sorted_string


# Example usage
print(sort_numbers('three one five'))  # Output: 'one three five'
```

This script defines a function `sort_numbers` that takes a space-delimited string of numberals as input, sorts them in ascending order, and returns the sorted string. The sorting is done using a dictionary to map numberals to their integer values. The example usage demonstrates how to use the `sort_numbers` function.