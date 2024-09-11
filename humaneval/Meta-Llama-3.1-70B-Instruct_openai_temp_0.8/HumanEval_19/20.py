```python
from typing import List

def sort_numbers(numbers: str) -> str:
    """
    This function takes a space-delimited string of numberals from 'zero' to 'nine' 
    and returns the string with numbers sorted from smallest to largest.

    Args:
        numbers (str): A space-delimited string of numberals.

    Returns:
        str: The input string with numbers sorted from smallest to largest.
    """

    # Create a dictionary to map number words to their integer values
    num_map = {
        'zero': 0, 'one': 1, 'two': 2, 'three': 3, 'four': 4, 
        'five': 5,'six': 6,'seven': 7, 'eight': 8, 'nine': 9
    }

    # Split the input string into a list of number words
    num_list: List[str] = numbers.split()

    # Sort the list of number words based on their integer values
    num_list.sort(key=lambda x: num_map[x])

    # Join the sorted list of number words back into a string
    sorted_numbers =''.join(num_list)

    return sorted_numbers


# Test the function
print(sort_numbers('three one five'))  # Output: 'one three five'
```
This script defines a function `sort_numbers` that sorts a space-delimited string of number words from 'zero' to 'nine' in ascending order. It uses a dictionary to map number words to their integer values and then sorts the list of number words based on these values. The sorted list is then joined back into a string and returned.