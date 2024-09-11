```python
from typing import List

def sort_numbers(numbers: str) -> str:
    """
    Sorts a space-delimited string of numberals from 'zero' to 'nine' in ascending order.

    Args:
        numbers (str): A space-delimited string of numberals.

    Returns:
        str: The input string with numbers sorted from smallest to largest.
    """
    # Define a dictionary to map number words to their integer equivalents
    num_map = {
        'zero': 0, 'one': 1, 'two': 2, 'three': 3, 'four': 4,
        'five': 5,'six': 6,'seven': 7, 'eight': 8, 'nine': 9
    }

    # Split the input string into a list of number words
    num_list = numbers.split()

    # Convert number words to integers, sort them, and then convert back to words
    sorted_num_list = [k for k, v in sorted(num_map.items(), key=lambda item: item[1]) if k in num_list]

    # Join the sorted number words back into a string
    sorted_numbers =''.join(sorted_num_list)

    return sorted_numbers


# Test the function
print(sort_numbers('three one five'))  # Expected output: 'one three five'
print(sort_numbers('eight two six four nine'))  # Expected output: 'two four six eight nine'
```