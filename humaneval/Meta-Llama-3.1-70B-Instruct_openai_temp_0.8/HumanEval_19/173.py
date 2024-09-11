```python
from typing import List

def sort_numbers(numbers: str) -> str:
    """
    This function takes a space-delimited string of numberals from 'zero' to 'nine' 
    and returns the string with numbers sorted from smallest to largest.

    Args:
        numbers (str): A space-delimited string of numberals.

    Returns:
        str: A space-delimited string with the numbers sorted from smallest to largest.
    """

    # Define the order of the numberals
    numeral_order = {
        'zero': 0, 'one': 1, 'two': 2, 'three': 3, 'four': 4, 
        'five': 5,'six': 6,'seven': 7, 'eight': 8, 'nine': 9
    }

    # Split the input string into a list of numberals
    numeral_list: List[str] = numbers.split()

    # Sort the list based on the order of the numberals
    sorted_numerals = sorted(numeral_list, key=lambda x: numeral_order[x])

    # Join the sorted list back into a string
    sorted_numbers =''.join(sorted_numerals)

    return sorted_numbers

# Test the function
print(sort_numbers('three one five'))  # Output: 'one three five'
```
This script defines a function `sort_numbers` that takes a string of space-delimited numberals, splits it into a list, sorts the list based on the order of the numberals, and joins the sorted list back into a string. The order of the numberals is defined in the `numeral_order` dictionary. The function uses the `sorted` function with a lambda function as the key to sort the list. The lambda function looks up the order of each numeral in the `numeral_order` dictionary.