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
    # Define a dictionary to map number names to their corresponding integer values
    num_dict = {
        'zero': 0, 'one': 1, 'two': 2, 'three': 3, 'four': 4,
        'five': 5,'six': 6,'seven': 7, 'eight': 8, 'nine': 9
    }

    # Split the input string into a list of number names
    num_list: List[str] = numbers.split()

    # Use a lambda function as the key for sorting, which returns the integer value of each number
    num_list.sort(key=lambda x: num_dict[x])

    # Join the sorted list back into a string separated by spaces
    sorted_string: str =''.join(num_list)

    return sorted_string


# Test the function
print(sort_numbers('three one five'))  # Output: 'one three five'
```
This script defines a function called `sort_numbers` that takes a space-delimited string of number names, sorts them in ascending order based on their integer values, and returns the sorted string. The test at the end of the script demonstrates the function's usage and output.