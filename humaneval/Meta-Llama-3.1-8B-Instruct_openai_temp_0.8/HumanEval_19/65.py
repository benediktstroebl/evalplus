```python
from typing import List

def sort_numbers(numbers: str) -> str:
    """
    Sorts a space-delimited string of numbers from 'zero' to 'nine' from smallest to largest.

    Args:
    numbers (str): A space-delimited string of numberals from 'zero' to 'nine'.

    Returns:
    str: The string with numbers sorted from smallest to largest.

    Examples:
    >>> sort_numbers('three one five')
    'one three five'
    """
    # Define a dictionary to map number strings to their corresponding integer values
    number_values = {
        'zero': 0, 'one': 1, 'two': 2, 'three': 3, 'four': 4,
        'five': 5,'six': 6,'seven': 7, 'eight': 8, 'nine': 9
    }

    # Split the input string into a list of numbers
    num_list: List[str] = numbers.split()

    # Sort the list of numbers based on their integer values
    num_list.sort(key=lambda x: number_values[x])

    # Join the sorted list of numbers back into a string
    sorted_numbers: str =''.join(num_list)

    return sorted_numbers

# Test the function
print(sort_numbers('three one five'))  # Output: 'one three five'
print(sort_numbers('nine eight seven'))  # Output:'seven eight nine'
```

In this script, we first define a dictionary `number_values` to map each number string to its corresponding integer value. We then split the input string into a list of numbers using the `split()` method. The `sort()` method is used to sort the list of numbers based on their integer values, which are retrieved using the `number_values` dictionary. Finally, we join the sorted list of numbers back into a string using the `join()` method and return the result.