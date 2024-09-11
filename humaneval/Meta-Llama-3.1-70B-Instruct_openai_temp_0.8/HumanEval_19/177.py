```python
from typing import List, Dict

# Dictionary mapping number words to their numerical values
NUMBER_MAPPING: Dict[str, int] = {
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
    # Split the input string into a list of number words
    number_list: List[str] = numbers.split()

    # Sort the list based on the numerical values of the number words
    sorted_list: List[str] = sorted(number_list, key=lambda x: NUMBER_MAPPING[x])

    # Join the sorted list back into a string separated by spaces
    sorted_string: str =''.join(sorted_list)

    return sorted_string

# Example usage
print(sort_numbers('three one five'))  # Output: 'one three five'
```

This script defines a function `sort_numbers` that takes a space-delimited string of number words as input, sorts them based on their numerical values, and returns the sorted string. The `NUMBER_MAPPING` dictionary is used to map number words to their corresponding numerical values. The `sorted` function is used with a lambda function as the `key` argument to sort the list of number words based on their numerical values.