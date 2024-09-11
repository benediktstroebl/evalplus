```python
from typing import List

def sort_numbers(numbers: str) -> str:
    """
    Sorts a space-delimited string of numberals from 'zero' to 'nine' in ascending order.

    Args:
        numbers (str): A string containing numberals separated by spaces.

    Returns:
        str: The input string with numberals sorted from smallest to largest.

    Raises:
        ValueError: If the input string contains invalid numberals.
    """
    # Define a dictionary to map numberals to their corresponding integer values
    num_map = {
        'zero': 0, 'one': 1, 'two': 2, 'three': 3, 'four': 4,
        'five': 5,'six': 6,'seven': 7, 'eight': 8, 'nine': 9
    }

    # Split the input string into a list of numberals
    num_list: List[str] = numbers.split()

    # Check if all numberals in the list are valid
    if not all(num in num_map for num in num_list):
        raise ValueError("Invalid numeral in input string")

    # Sort the list of numberals based on their integer values
    sorted_num_list: List[str] = sorted(num_list, key=lambda num: num_map[num])

    # Join the sorted list of numberals back into a string
    sorted_numbers: str =''.join(sorted_num_list)

    return sorted_numbers


# Test the function
print(sort_numbers('three one five'))  # Output: 'one three five'
```