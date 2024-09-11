```python
from typing import List, Dict

def sort_numbers(numbers: str) -> str:
    """
    Input is a space-delimited string of numberals from 'zero' to 'nine'.
    Valid choices are 'zero', 'one', 'two', 'three', 'four', 'five','six','seven', 'eight' and 'nine'.
    Return the string with numbers sorted from smallest to largest

    :param numbers: A space-delimited string of numberals
    :return: The string with numbers sorted from smallest to largest
    """

    # Define a dictionary to map number words to their numerical values
    number_map: Dict[str, int] = {
        'zero': 0, 'one': 1, 'two': 2, 'three': 3, 'four': 4,
        'five': 5,'six': 6,'seven': 7, 'eight': 8, 'nine': 9
    }

    # Split the input string into a list of number words
    number_list: List[str] = numbers.split()

    # Sort the list of number words based on their numerical values
    sorted_number_list: List[str] = sorted(number_list, key=lambda x: number_map[x])

    # Join the sorted list of number words back into a string
    sorted_numbers: str =''.join(sorted_number_list)

    return sorted_numbers


# Test the function
print(sort_numbers('three one five'))  # Output: 'one three five'
```

This script first defines a dictionary to map number words to their numerical values. It then splits the input string into a list of number words, sorts this list based on the numerical values, and finally joins the sorted list back into a string. The result is a string with the number words sorted from smallest to largest.