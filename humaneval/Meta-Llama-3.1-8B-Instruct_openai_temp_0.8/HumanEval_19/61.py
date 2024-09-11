```python
from typing import List

def sort_numbers(numbers: str) -> str:
    """
    Input is a space-delimited string of numberals from 'zero' to 'nine'.
    Valid choices are 'zero', 'one', 'two', 'three', 'four', 'five','six','seven', 'eight' and 'nine'.
    Return the string with numbers sorted from smallest to largest
    """
    # Define a dictionary to map word numbers to their integer values
    num_map = {
        'zero': 0, 'one': 1, 'two': 2, 'three': 3, 'four': 4,
        'five': 5,'six': 6,'seven': 7, 'eight': 8, 'nine': 9
    }

    # Split the input string into a list of word numbers
    numbers_list: List[str] = numbers.split()

    # Sort the list of word numbers based on their integer values
    numbers_list.sort(key=lambda x: num_map[x])

    # Join the sorted list back into a string
    sorted_numbers: str =''.join(numbers_list)

    return sorted_numbers


# Test the function
print(sort_numbers('three one five'))  # Output: 'one three five'
```

This script defines a function `sort_numbers` that takes a space-delimited string of word numbers as input, sorts them based on their integer values, and returns the sorted string. The function uses a dictionary to map word numbers to their integer values, and the built-in `sort` method with a lambda function as the `key` argument to sort the list of word numbers. The sorted list is then joined back into a string using the `join` method.