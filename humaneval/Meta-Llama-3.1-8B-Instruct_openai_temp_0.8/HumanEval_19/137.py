```python
from typing import List, Dict

# Define a dictionary to map string numbers to integers
num_map: Dict[str, int] = {
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

    # Sort the list of numbers based on their integer values
    sorted_list: List[str] = sorted(num_list, key=lambda x: num_map[x])

    # Join the sorted list back into a string
    sorted_string: str =''.join(sorted_list)

    return sorted_string

# Example usage:
print(sort_numbers('three one five'))  # Output: 'one three five'
print(sort_numbers('nine five zero'))  # Output: 'zero five nine'
```

In this script, we first define a dictionary `num_map` to map string numbers to integers. We then use the built-in `split` method to split the input string into a list of numbers. The `sorted` function is used to sort this list based on the integer values, which we retrieve from the `num_map` dictionary using a lambda function as the `key` argument. Finally, we join the sorted list back into a string using the `join` method, and return the result.