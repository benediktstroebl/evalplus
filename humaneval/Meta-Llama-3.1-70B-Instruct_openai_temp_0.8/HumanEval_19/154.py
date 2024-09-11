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

    # Define a dictionary to map number words to their integer values
    num_dict = {
        'zero': 0, 'one': 1, 'two': 2, 'three': 3, 'four': 4,
        'five': 5,'six': 6,'seven': 7, 'eight': 8, 'nine': 9
    }

    # Split the input string into a list of number words
    num_list = numbers.split()

    # Sort the list of number words based on their integer values
    sorted_list = sorted(num_list, key=lambda x: num_dict[x])

    # Join the sorted list back into a string
    sorted_str =''.join(sorted_list)

    return sorted_str

# Test the function
print(sort_numbers('three one five'))  # Output: 'one three five'
```

This script first defines a dictionary `num_dict` to map number words to their integer values. Then it splits the input string into a list of number words, sorts the list based on the integer values of the number words, and finally joins the sorted list back into a string. The result is a string with the number words sorted from smallest to largest.