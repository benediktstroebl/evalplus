### Number Sorter Script
```markdown
### Problem Description
Input is a space-delimited string of numerical words from 'zero' to 'nine'.
Valid choices are 'zero', 'one', 'two', 'three', 'four', 'five','six','seven', 'eight', and 'nine'.
Return the string with numbers sorted from smallest to largest.

### Solution

```python
from typing import List

def num_dict() -> dict:
    """ Create a dictionary of numbers and their integer values """
    num_dict = {
        'zero': 0, 'one': 1, 'two': 2, 'three': 3, 'four': 4,
        'five': 5,'six': 6,'seven': 7, 'eight': 8, 'nine': 9
    }
    return num_dict

def sort_numbers(numbers: str) -> str:
    """ Input is a space-delimited string of numerical words from 'zero' to 'nine'.
    Return the string with numbers sorted from smallest to largest """
    num_values = num_dict()
    # Split the input string into a list of numerical words
    num_list: List[str] = numbers.split()
    
    # Sort the list based on the integer values of the numerical words
    sorted_num_list = sorted(num_list, key=lambda x: num_values[x])
    
    # Join the sorted list into a string
    sorted_string =''.join(sorted_num_list)
    
    return sorted_string

# Example usage:
if __name__ == "__main__":
    print(sort_numbers('three one five'))  # Output: 'one three five'
```

### Explanation

This script defines a function `num_dict()` that creates a dictionary mapping numerical words to their integer values. The `sort_numbers()` function uses this dictionary to sort a list of numerical words based on their integer values.

The script then sorts the input string into a list of numerical words, sorts the list, and joins it back into a string. Finally, it prints the sorted string.

Note that this script uses a lambda function as the key for the `sorted()` function, which allows it to sort the list based on the dictionary values.