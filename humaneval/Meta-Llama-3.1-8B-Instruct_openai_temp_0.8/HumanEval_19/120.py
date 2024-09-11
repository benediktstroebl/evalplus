### Numerical String Sorter

Below is a Python script that defines a function to sort numbers in a string:

```markdown
### Code
```python
from typing import Dict

def sort_numbers(numbers: str) -> str:
    """
    Input is a space-delimited string of numberals from 'zero' to 'nine'.
    Valid choices are 'zero', 'one', 'two', 'three', 'four', 'five','six','seven', 'eight' and 'nine'.
    Return the string with numbers sorted from smallest to largest
    >>> sort_numbers('three one five')
    'one three five'
    """
    # Create a dictionary to map string representations of numbers to their integer values
    num_dict: Dict[str, int] = {
        'zero': 0, 'one': 1, 'two': 2, 'three': 3, 'four': 4, 'five': 5,
       'six': 6,'seven': 7, 'eight': 8, 'nine': 9
    }
    
    # Split the input string into a list of strings
    num_list: List[str] = numbers.split()
    
    # Sort the list of strings based on their integer values
    sorted_list: List[str] = sorted(num_list, key=lambda x: num_dict[x])
    
    # Join the sorted list into a string
    sorted_string: str =''.join(sorted_list)
    
    return sorted_string

### Example Usage
numbers: str = 'three one five'
sorted_numbers: str = sort_numbers(numbers)
print(f"Sorted numbers: {sorted_numbers}")
```

### Explanation

This script defines a function `sort_numbers` that takes a string of space-delimited numbers as input and returns a string with the numbers sorted from smallest to largest.

Here's a step-by-step breakdown of the function:

1. Create a dictionary `num_dict` to map string representations of numbers to their integer values.
2. Split the input string into a list of strings using the `split()` method.
3. Sort the list of strings based on their integer values using the `sorted()` function and a lambda function as the `key` argument. The lambda function looks up the integer value of each string in the `num_dict` dictionary.
4. Join the sorted list into a string using the `join()` method.
5. Return the sorted string.

The example usage demonstrates how to call the `sort_numbers` function with a sample input string and print the sorted result.