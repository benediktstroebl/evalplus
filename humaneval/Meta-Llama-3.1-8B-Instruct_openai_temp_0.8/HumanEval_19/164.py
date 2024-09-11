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
    # Create a dictionary to map number strings to their integer values
    number_mapping = {
        'zero': 0, 'one': 1, 'two': 2, 'three': 3, 'four': 4,
        'five': 5,'six': 6,'seven': 7, 'eight': 8, 'nine': 9
    }

    # Split the input string into a list of numbers
    num_list: List[str] = numbers.split()

    # Sort the list of numbers based on their integer values
    num_list.sort(key=lambda x: number_mapping[x])

    # Join the sorted list back into a string separated by spaces
    sorted_numbers: str =''.join(num_list)

    return sorted_numbers


# Test the function
print(sort_numbers('three one five'))  # Output: 'one three five'
print(sort_numbers('nine eight seven'))  # Output:'seven eight nine'
```

This script first creates a dictionary to map each number string to its corresponding integer value. It then splits the input string into a list of numbers, sorts this list based on the integer values, and finally joins the sorted list back into a string separated by spaces. The sorted string is then returned as the result.