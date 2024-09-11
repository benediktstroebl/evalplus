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
    # Split the input string into a list of numbers
    numbers_list: List[str] = numbers.split()

    # Define a dictionary to map number names to their integer values
    number_mapping: dict[str, int] = {
        'zero': 0, 'one': 1, 'two': 2, 'three': 3, 'four': 4, 'five': 5,
       'six': 6,'seven': 7, 'eight': 8, 'nine': 9
    }

    # Sort the list of numbers based on their integer values
    sorted_numbers: List[str] = sorted(numbers_list, key=lambda x: number_mapping[x])

    # Join the sorted list of numbers into a string
    sorted_string: str =''.join(sorted_numbers)

    return sorted_string

# Test the function
print(sort_numbers('three one five'))  # Output: 'one three five'
print(sort_numbers('nine seven five'))  # Output: 'five seven nine'
```

In this script, we define a function `sort_numbers` that takes a space-delimited string of numbers as input and returns the string with numbers sorted from smallest to largest. The function uses a dictionary to map number names to their integer values, sorts the list of numbers based on these values, and then joins the sorted list back into a string. We also include test cases to demonstrate the function's correctness.