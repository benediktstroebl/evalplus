```python
from typing import Dict

def sort_numbers(numbers: str) -> str:
    """
    Input is a space-delimited string of numberals from 'zero' to 'nine'.
    Valid choices are 'zero', 'one', 'two', 'three', 'four', 'five','six','seven', 'eight' and 'nine'.
    Return the string with numbers sorted from smallest to largest

    Args:
        numbers (str): A space-delimited string of numbers

    Returns:
        str: The sorted string of numbers

    Example:
        >>> sort_numbers('three one five')
        'one three five'
    """

    # Create a dictionary to map number strings to their integer values
    number_dict: Dict[str, int] = {
        'zero': 0, 'one': 1, 'two': 2, 'three': 3, 'four': 4,
        'five': 5,'six': 6,'seven': 7, 'eight': 8, 'nine': 9
    }

    # Split the input string into a list of numbers
    num_list: List[str] = numbers.split()

    # Sort the list of numbers based on their integer values
    sorted_num_list: List[str] = sorted(num_list, key=lambda x: number_dict[x])

    # Join the sorted list back into a string separated by spaces
    sorted_string: str =''.join(sorted_num_list)

    return sorted_string

# Example usage:
print(sort_numbers('three one five'))
print(sort_numbers('seven eight nine'))
print(sort_numbers('nine eight seven'))
print(sort_numbers('zero one two three four five six seven eight nine'))
```

This script first maps the number strings to their integer values, then splits the input string into a list of numbers, sorts the list based on these integer values, and finally joins the sorted list back into a string. The `sorted` function is used with a lambda function as the `key` argument to specify the sorting criteria.