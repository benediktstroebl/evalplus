```python
from typing import List

def sort_numbers(numbers: str) -> str:
    """
    Input is a space-delimited string of numberals from 'zero' to 'nine'.
    Valid choices are 'zero', 'one', 'two', 'three', 'four', 'five','six','seven', 'eight' and 'nine'.
    Return the string with numbers sorted from smallest to largest

    Args:
        numbers (str): A space-delimited string of numbers.

    Returns:
        str: The input string with numbers sorted from smallest to largest.
    """

    # Define a dictionary to map string numbers to their integer equivalents
    num_dict = {
        'zero': 0, 'one': 1, 'two': 2, 'three': 3, 'four': 4,
        'five': 5,'six': 6,'seven': 7, 'eight': 8, 'nine': 9
    }

    # Split the input string into a list of numbers
    num_list: List[str] = numbers.split()

    # Sort the list of numbers based on their integer equivalents
    num_list.sort(key=lambda x: num_dict[x])

    # Join the sorted list into a string with spaces in between
    sorted_str: str =''.join(num_list)

    return sorted_str


# Example usage:
print(sort_numbers('three one five'))  # Output: 'one three five'
print(sort_numbers('eight nine seven'))  # Output:'seven eight nine'
```

This script defines a function called `sort_numbers` that takes a space-delimited string of numbers as input and returns the string with numbers sorted from smallest to largest. The function uses a dictionary to map string numbers to their integer equivalents and then sorts the list of numbers based on these equivalents. The sorted list is then joined back into a string with spaces in between. The script includes example usage at the end to demonstrate how to call the function.