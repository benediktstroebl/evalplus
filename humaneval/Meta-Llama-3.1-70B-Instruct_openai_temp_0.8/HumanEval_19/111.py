```python
from typing import List

def sort_numbers(numbers: str) -> str:
    """
    Sorts a space-delimited string of numberals from 'zero' to 'nine' in ascending order.

    Args:
        numbers (str): A space-delimited string of numberals.

    Returns:
        str: The input string with numbers sorted from smallest to largest.

    Examples:
        >>> sort_numbers('three one five')
        'one three five'
    """
    # Define a dictionary to map number words to their integer values
    num_dict = {
        'zero': 0, 'one': 1, 'two': 2, 'three': 3, 'four': 4,
        'five': 5,'six': 6,'seven': 7, 'eight': 8, 'nine': 9
    }

    # Split the input string into a list of number words
    num_list: List[str] = numbers.split()

    # Sort the list of number words based on their integer values
    num_list.sort(key=lambda x: num_dict[x])

    # Join the sorted list back into a string
    sorted_numbers =''.join(num_list)

    return sorted_numbers


# Test the function
print(sort_numbers('three one five'))  # Output: 'one three five'
```

This script works by first defining a dictionary that maps number words to their integer values. It then splits the input string into a list of number words, sorts this list based on the integer values of the number words, and finally joins the sorted list back into a string.