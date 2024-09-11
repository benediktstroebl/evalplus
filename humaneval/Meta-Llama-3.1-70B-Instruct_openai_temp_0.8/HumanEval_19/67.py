```python
from typing import List

def sort_numbers(numbers: str) -> str:
    """
    Sorts a space-delimited string of numberals from 'zero' to 'nine' in ascending order.

    Args:
        numbers (str): A string containing numberals separated by spaces.

    Returns:
        str: The input string with numbers sorted from smallest to largest.
    """
    
    # Define a dictionary mapping numberals to their integer values
    numeral_map = {
        'zero': 0, 'one': 1, 'two': 2, 'three': 3, 'four': 4,
        'five': 5,'six': 6,'seven': 7, 'eight': 8, 'nine': 9
    }

    # Split the input string into a list of numberals
    numeral_list: List[str] = numbers.split()

    # Sort the list of numberals based on their integer values
    sorted_numerals = sorted(numeral_list, key=lambda x: numeral_map[x])

    # Join the sorted list of numberals back into a string separated by spaces
    sorted_string =''.join(sorted_numerals)

    return sorted_string


# Example usage
print(sort_numbers('three one five'))  # Output: 'one three five'
print(sort_numbers('eight two six four'))  # Output: 'two four six eight'
```

In this script, we first define a dictionary `numeral_map` that maps numberals to their integer values. We then split the input string into a list of numberals using the `split()` method. The list is sorted using the `sorted()` function with a lambda function as the key, which looks up the integer value of each numeral in the `numeral_map` dictionary. Finally, we join the sorted list of numberals back into a string separated by spaces using the `join()` method.