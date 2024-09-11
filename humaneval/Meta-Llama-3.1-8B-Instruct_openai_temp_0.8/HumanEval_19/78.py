```python
from typing import List, Dict

def sort_numbers(numbers: str) -> str:
    """
    Input is a space-delimited string of numberals from 'zero' to 'nine'.
    Valid choices are 'zero', 'one', 'two', 'three', 'four', 'five','six','seven', 'eight' and 'nine'.
    Return the string with numbers sorted from smallest to largest

    Args:
        numbers (str): A space-delimited string of numberals.

    Returns:
        str: The string with numbers sorted from smallest to largest.
    """
    # Create a dictionary for mapping number words to their integer values
    num_dict: Dict[str, int] = {
        'zero': 0, 'one': 1, 'two': 2, 'three': 3, 'four': 4,
        'five': 5,'six': 6,'seven': 7, 'eight': 8, 'nine': 9
    }

    # Split the input string into a list of numbers
    num_list: List[str] = numbers.split()

    # Sort the list of numbers based on their integer values
    sorted_list: List[str] = sorted(num_list, key=lambda x: num_dict[x])

    # Join the sorted list into a string separated by spaces
    sorted_string: str =''.join(sorted_list)

    return sorted_string

# Test the function
print(sort_numbers('three one five'))  # Output: 'one three five'
print(sort_numbers('five six zero four'))  # Output: 'zero four five six'
```

This Python script defines a function `sort_numbers` that takes a space-delimited string of numberals as input, sorts them from smallest to largest, and returns the sorted string. The function uses a dictionary to map number words to their integer values and the built-in `sorted` function with a custom sorting key to achieve the sorting.