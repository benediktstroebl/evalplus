Here's a Python script that sorts a string of numbers from 'zero' to 'nine' in ascending order.

```python
from typing import List, Tuple

# Dictionary to map numerical words to their integer values
num_dict = {
    'zero': 0, 'one': 1, 'two': 2, 'three': 3, 'four': 4,
    'five': 5,'six': 6,'seven': 7, 'eight': 8, 'nine': 9
}

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

    # Convert the list of numbers to a list of integers using the num_dict
    num_list = [num_dict[num] for num in num_list]

    # Sort the list of integers in ascending order
    num_list.sort()

    # Convert the sorted list of integers back to a list of strings using the num_dict
    sorted_num_list: List[str] = [num_dict[num] for num in num_list]

    # Join the sorted list of strings back into a string with spaces in between
    sorted_string: str =''.join(sorted_num_list)

    return sorted_string

# Test the function
print(sort_numbers('three one five'))  # Expected output: 'one three five'
```

This script works as follows:

- It defines a dictionary `num_dict` to map numerical words to their integer values.
- The `sort_numbers` function takes a string of numbers as input, splits it into a list of numbers, and converts each number to its integer value using the `num_dict`.
- The list of integers is then sorted in ascending order using the built-in `sort` method.
- Finally, the sorted list of integers is converted back to a list of strings and joined back into a string with spaces in between, which is then returned.