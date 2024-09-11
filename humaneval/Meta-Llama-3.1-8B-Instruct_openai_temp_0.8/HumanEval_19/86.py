```python
from typing import List


def sort_numbers(numbers: str) -> str:
    """
    Input is a space-delimited string of numberals from 'zero' to 'nine'.
    Valid choices are 'zero', 'one', 'two', 'three', 'four', 'five','six','seven', 'eight' and 'nine'.
    Return the string with numbers sorted from smallest to largest.

    Args:
        numbers (str): A space-delimited string of numbers.

    Returns:
        str: The input string with numbers sorted from smallest to largest.
    """
    # Split the input string into a list of numbers
    num_list: List[str] = numbers.split()

    # Create a dictionary to map string numbers to their integer equivalents
    num_dict: dict = {'zero': 0, 'one': 1, 'two': 2, 'three': 3, 'four': 4, 'five': 5,
                     'six': 6,'seven': 7, 'eight': 8, 'nine': 9}

    # Sort the list of numbers based on their integer equivalents
    sorted_list: List[str] = sorted(num_list, key=lambda x: num_dict[x])

    # Join the sorted list into a string with spaces in between
    sorted_string: str =''.join(sorted_list)

    return sorted_string


# Example usage:
print(sort_numbers('three one five'))  # Output: 'one three five'
print(sort_numbers('nine eight seven'))  # Output: 'eight nine seven'
```
This script uses a dictionary to map the string numbers to their integer equivalents, allowing the function to sort the numbers based on their numerical value. The sorted list of numbers is then joined back into a string with spaces in between, which is the final output.