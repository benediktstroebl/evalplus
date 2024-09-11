### Sorting Numbers in a String
#### Problem Description
Given a string of numbers (with words 'zero' to 'nine'), return the string with numbers sorted from smallest to largest.

#### Solution
Here's a Python function to solve this problem. This function works by first creating a dictionary to map the word representations of numbers to their integer values. It then splits the input string into a list of numbers, sorts the list based on the corresponding integer values, and finally joins the sorted numbers back into a string.

```python
from typing import List

def sort_numbers(numbers: str) -> str:
    """ Input is a space-delimited string of numberals from 'zero' to 'nine'.
    Valid choices are 'zero', 'one', 'two', 'three', 'four', 'five','six','seven', 'eight' and 'nine'.
    Return the string with numbers sorted from smallest to largest
    >>> sort_numbers('three one five')
    'one three five'
    """
    # Create a dictionary to map word representations to integer values
    num_dict = {
        'zero': 0, 'one': 1, 'two': 2, 'three': 3, 'four': 4,
        'five': 5,'six': 6,'seven': 7, 'eight': 8, 'nine': 9
    }

    # Split the input string into a list of numbers
    num_list: List[str] = numbers.split()

    # Sort the list based on the corresponding integer values
    sorted_list: List[str] = sorted(num_list, key=lambda x: num_dict[x])

    # Join the sorted numbers back into a string
    sorted_string: str =''.join(sorted_list)

    return sorted_string

# Example usage:
print(sort_numbers('three one five'))  # Output: 'one three five'
```

This script includes a docstring that describes the function and its expected input and output, as well as an example usage of the function. The `num_dict` dictionary maps the word representations of numbers to their integer values, allowing for efficient sorting of the numbers in the input string.