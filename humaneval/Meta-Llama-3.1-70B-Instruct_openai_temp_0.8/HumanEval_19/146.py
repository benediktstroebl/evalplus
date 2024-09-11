```python
from typing import List, Dict

def sort_numbers(numbers: str) -> str:
    """
    Input is a space-delimited string of numberals from 'zero' to 'nine'.
    Valid choices are 'zero', 'one', 'two', 'three', 'four', 'five','six','seven', 'eight' and 'nine'.
    Return the string with numbers sorted from smallest to largest

    :param numbers: A space-delimited string of numberals
    :return: A string with numbers sorted from smallest to largest
    """

    # Create a dictionary to map number words to their integer values
    number_mapping: Dict[str, int] = {
        'zero': 0, 'one': 1, 'two': 2, 'three': 3, 'four': 4, 'five': 5,
       'six': 6,'seven': 7, 'eight': 8, 'nine': 9
    }

    # Split the input string into a list of number words
    number_list: List[str] = numbers.split()

    # Sort the list of number words based on their integer values
    sorted_numbers: List[str] = sorted(number_list, key=lambda x: number_mapping[x])

    # Join the sorted number words back into a string
    sorted_string: str =''.join(sorted_numbers)

    return sorted_string


# Example usage
print(sort_numbers('three one five'))  # Output: 'one three five'
```

This script works by first creating a dictionary to map number words to their integer values. It then splits the input string into a list of number words and sorts this list based on the integer values of the number words. Finally, it joins the sorted number words back into a string and returns this string.