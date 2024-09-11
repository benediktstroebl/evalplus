```python
from typing import List, Dict

def sort_numbers(numbers: str) -> str:
    """
    Input is a space-delimited string of numberals from 'zero' to 'nine'.
    Valid choices are 'zero', 'one', 'two', 'three', 'four', 'five','six','seven', 'eight' and 'nine'.
    Return the string with numbers sorted from smallest to largest

    Args:
        numbers (str): A space-delimited string of numberals

    Returns:
        str: The string with numbers sorted from smallest to largest
    """

    # Create a dictionary to map numberals to their corresponding integer values
    numeral_map: Dict[str, int] = {
        'zero': 0, 'one': 1, 'two': 2, 'three': 3, 'four': 4,
        'five': 5,'six': 6,'seven': 7, 'eight': 8, 'nine': 9
    }

    # Split the input string into a list of numberals
    numeral_list: List[str] = numbers.split()

    # Sort the list of numberals based on their corresponding integer values
    sorted_numerals: List[str] = sorted(numeral_list, key=lambda x: numeral_map[x])

    # Join the sorted list of numberals back into a string
    sorted_string: str =''.join(sorted_numerals)

    return sorted_string


# Test the function
print(sort_numbers('three one five'))  # Output: 'one three five'
```

In this script, we define a dictionary `numeral_map` to map each numeral to its corresponding integer value. We then split the input string into a list of numberals, sort the list based on the integer values, and finally join the sorted list back into a string.

The `sorted` function is used with a custom sorting key, which is a lambda function that looks up the integer value of each numeral in the `numeral_map` dictionary. This allows us to sort the numberals in ascending order based on their integer values.