```python
from typing import Dict

# Function to convert number strings to integers for sorting
def string_to_int(num_str: str) -> int:
    """ Helper function to convert number string to integer """
    num_dict: Dict[str, int] = {
        'zero': 0, 'one': 1, 'two': 2, 'three': 3, 'four': 4,
        'five': 5,'six': 6,'seven': 7, 'eight': 8, 'nine': 9
    }
    return num_dict[num_str]

# Function to sort numbers in a string
def sort_numbers(numbers: str) -> str:
    """
    Input is a space-delimited string of numberals from 'zero' to 'nine'.
    Valid choices are 'zero', 'one', 'two', 'three', 'four', 'five','six','seven', 'eight' and 'nine'.
    Return the string with numbers sorted from smallest to largest
    >>> sort_numbers('three one five')
    'one three five'
    """
    # Split the input string into a list of numbers
    num_list: List[str] = numbers.split()

    # Use a custom sorting function to sort the list
    sorted_list: List[str] = sorted(num_list, key=string_to_int)

    # Join the sorted list back into a string separated by spaces
    sorted_str: str =''.join(sorted_list)

    return sorted_str

# Test the function
print(sort_numbers('three one five'))  # Output: 'one three five'
```

This script defines a custom sorting function `sort_numbers` that uses a dictionary to convert the number strings to integers for sorting, and then sorts the list of numbers in ascending order. The sorted list is then joined back into a string separated by spaces. The test at the end of the script demonstrates the function's usage.