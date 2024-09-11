### Sorting Numbers in a String

The following Python script defines a function `sort_numbers` that takes a space-delimited string of numbers from 'zero' to 'nine', sorts them in ascending order, and returns the sorted string.

```markdown
### Code
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
    str: The sorted string.

    >>> sort_numbers('three one five')
    'one three five'
    """
    
    # Create a dictionary to map string numbers to their integer values
    num_dict = {
        'zero': 0, 'one': 1, 'two': 2, 'three': 3, 'four': 4,
        'five': 5,'six': 6,'seven': 7, 'eight': 8, 'nine': 9
    }

    # Split the input string into a list of numbers
    num_list = numbers.split()

    # Sort the list of numbers based on their integer values
    num_list.sort(key=lambda x: num_dict[x])

    # Join the sorted list into a string
    sorted_str =''.join(num_list)

    return sorted_str

# Example usage:
print(sort_numbers('three one five'))  # Output: 'one three five'
print(sort_numbers('seven eight nine'))  # Output:'seven eight nine'
```

### Explanation

The `sort_numbers` function works as follows:

1.  Create a dictionary `num_dict` that maps string numbers to their integer values.
2.  Split the input string into a list of numbers using the `split` method.
3.  Sort the list of numbers based on their integer values using the `sort` method and a lambda function as the `key` argument. The lambda function takes a string number, looks up its integer value in the `num_dict`, and returns this value.
4.  Join the sorted list into a string using the `join` method.
5.  Return the sorted string.