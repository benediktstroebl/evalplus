```python
from typing import List

def sort_numbers(numbers: str) -> str:
    """
    Input is a space-delimited string of numberals from 'zero' to 'nine'.
    Valid choices are 'zero', 'one', 'two', 'three', 'four', 'five','six','seven', 'eight' and 'nine'.
    Return the string with numbers sorted from smallest to largest

    Args:
        numbers (str): A space-delimited string of numberals.

    Returns:
        str: The input string with numbers sorted from smallest to largest.
    """
    # Define a dictionary to map string numbers to integer
    num_map = {
        'zero': 0, 'one': 1, 'two': 2, 'three': 3, 'four': 4,
        'five': 5,'six': 6,'seven': 7, 'eight': 8, 'nine': 9
    }

    # Split the input string into a list of string numbers
    num_list: List[str] = numbers.split()

    # Sort the list of string numbers based on their corresponding integer values
    sorted_num_list: List[str] = sorted(num_list, key=lambda x: num_map[x])

    # Join the sorted list into a string with spaces in between
    sorted_numbers: str =''.join(sorted_num_list)

    return sorted_numbers


# Test the function
print(sort_numbers('three one five'))  # Expected output: 'one three five'
print(sort_numbers('nine eight seven'))  # Expected output: 'eight seven nine'
print(sort_numbers('zero zero zero'))  # Expected output: 'zero zero zero'
```