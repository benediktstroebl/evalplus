```python
from typing import Dict, List

def sort_numbers(numbers: str) -> str:
    """
    This function takes a space-delimited string of numberals from 'zero' to 'nine', 
    and returns the string with numbers sorted from smallest to largest.

    Args:
        numbers (str): A space-delimited string of numberals.

    Returns:
        str: The string with numbers sorted from smallest to largest.
    """

    # Create a dictionary to map number words to their integer values
    num_dict: Dict[str, int] = {
        'zero': 0, 'one': 1, 'two': 2, 'three': 3, 'four': 4,
        'five': 5,'six': 6,'seven': 7, 'eight': 8, 'nine': 9
    }

    # Split the input string into a list of number words
    num_list: List[str] = numbers.split()

    # Sort the list of number words based on their integer values
    sorted_list: List[str] = sorted(num_list, key=lambda x: num_dict[x])

    # Join the sorted list of number words back into a string
    sorted_str: str =''.join(sorted_list)

    return sorted_str


# Test the function
print(sort_numbers('three one five'))  # Output: 'one three five'
```