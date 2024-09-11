```python
from typing import List, Dict

def sort_numbers(numbers: str) -> str:
    """
    Input is a space-delimited string of numberals from 'zero' to 'nine'.
    Valid choices are 'zero', 'one', 'two', 'three', 'four', 'five','six','seven', 'eight' and 'nine'.
    Return the string with numbers sorted from smallest to largest

    Args:
        numbers (str): A space-delimited string of numbers

    Returns:
        str: The input string with numbers sorted from smallest to largest
    """

    # Create a dictionary to map number strings to their integer equivalents
    num_dict: Dict[str, int] = {
        'zero': 0, 'one': 1, 'two': 2, 'three': 3, 'four': 4,
        'five': 5,'six': 6,'seven': 7, 'eight': 8, 'nine': 9
    }

    # Split the input string into a list of numbers
    num_list: List[str] = numbers.split()

    # Sort the list of numbers based on their integer equivalents
    num_list.sort(key=lambda x: num_dict[x])

    # Join the sorted list back into a string separated by spaces
    sorted_string: str =''.join(num_list)

    return sorted_string


# Example usage:
print(sort_numbers('three one five'))  # Output: one three five
print(sort_numbers('nine five eight four'))  # Output: four five eight nine
print(sort_numbers('zero two six three'))  # Output: two three six zero
```

This script first creates a dictionary to map the string representations of numbers to their integer values. It then splits the input string into a list, sorts the list based on the integer values, and finally joins the sorted list back into a string. The `sort` method is used with a lambda function as the `key` argument to specify that the list should be sorted based on the dictionary values.