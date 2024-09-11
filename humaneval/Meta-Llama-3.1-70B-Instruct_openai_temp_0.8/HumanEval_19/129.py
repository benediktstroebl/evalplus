```python
from typing import List

def sort_numbers(numbers: str) -> str:
    """
    Input is a space-delimited string of numberals from 'zero' to 'nine'.
    Valid choices are 'zero', 'one', 'two', 'three', 'four', 'five','six','seven', 'eight' and 'nine'.
    Return the string with numbers sorted from smallest to largest

    >>> sort_numbers('three one five')
    'one three five'
    """

    # Create a dictionary that maps the string representation of a number to its integer value
    number_mapping = {
        'zero': 0, 'one': 1, 'two': 2, 'three': 3, 'four': 4,
        'five': 5,'six': 6,'seven': 7, 'eight': 8, 'nine': 9
    }

    # Split the input string into a list of strings, each representing a number
    number_list: List[str] = numbers.split()

    # Sort the list of numbers based on their integer values
    sorted_numbers = sorted(number_list, key=lambda x: number_mapping[x])

    # Join the sorted list of numbers back into a string
    sorted_numbers_str =''.join(sorted_numbers)

    return sorted_numbers_str


# Example usage
print(sort_numbers('three one five'))  # Output: 'one three five'
```

This script works by first defining a dictionary that maps the string representation of each number to its integer value. It then splits the input string into a list of strings, each representing a number. The `sorted` function is used to sort this list, with a lambda function used as the key to specify that the sorting should be based on the integer values of the numbers. Finally, the sorted list is joined back into a string, which is returned as the result.