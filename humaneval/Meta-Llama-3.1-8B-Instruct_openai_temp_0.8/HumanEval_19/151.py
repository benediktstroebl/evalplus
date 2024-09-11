### Sort Numbers Script

```python
from typing import List

def sort_numbers(numbers: str) -> str:
    """
    Sorts a space-delimited string of numbers from 'zero' to 'nine' in ascending order.

    Args:
        numbers (str): A space-delimited string of numberals from 'zero' to 'nine'.

    Returns:
        str: The string with numbers sorted from smallest to largest.
    """
    # Define a dictionary to map string numbers to their integer equivalents
    num_dict = {
        'zero': 0, 'one': 1, 'two': 2, 'three': 3, 'four': 4,
        'five': 5,'six': 6,'seven': 7, 'eight': 8, 'nine': 9
    }

    # Split the input string into a list of numbers
    num_list: List[str] = numbers.split()

    # Sort the list of numbers based on their integer equivalents
    sorted_list: List[str] = sorted(num_list, key=lambda x: num_dict[x])

    # Join the sorted list back into a string
    sorted_string: str =''.join(sorted_list)

    return sorted_string

# Test the function
print(sort_numbers('three one five'))  # Output: 'one three five'
```

This script defines a function `sort_numbers` that takes a space-delimited string of numbers as input and returns the string with numbers sorted from smallest to largest. The function uses a dictionary to map string numbers to their integer equivalents, splits the input string into a list of numbers, sorts the list based on the integer equivalents, and joins the sorted list back into a string. The script then tests the function with an example input.