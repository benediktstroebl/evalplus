```python
from typing import List, Dict

def sort_numbers(numbers: str) -> str:
    """
    Input is a space-delimited string of numberals from 'zero' to 'nine'.
    Valid choices are 'zero', 'one', 'two', 'three', 'four', 'five','six','seven', 'eight' and 'nine'.
    Return the string with numbers sorted from smallest to largest

    Args:
    numbers (str): A space-delimited string of numberals.

    Returns:
    str: The string with numbers sorted from smallest to largest.
    """
    # Create a dictionary to map numberals to their integer values
    numeral_map: Dict[str, int] = {
        'zero': 0, 'one': 1, 'two': 2, 'three': 3, 'four': 4,
        'five': 5,'six': 6,'seven': 7, 'eight': 8, 'nine': 9
    }

    # Split the input string into a list of numberals
    numeral_list: List[str] = numbers.split()

    # Sort the list of numberals based on their integer values
    sorted_numerals: List[str] = sorted(numeral_list, key=lambda x: numeral_map[x])

    # Join the sorted list of numberals into a string
    sorted_string: str =''.join(sorted_numerals)

    return sorted_string

# Test the function
print(sort_numbers('three one five'))  # Output: 'one three five'
```

This Python script uses a dictionary to map numberals to their integer values, allowing for easy sorting. The `sorted` function is used with a lambda function as the `key` argument to sort the list of numberals based on their integer values. The sorted list is then joined back into a string, which is returned as the result.