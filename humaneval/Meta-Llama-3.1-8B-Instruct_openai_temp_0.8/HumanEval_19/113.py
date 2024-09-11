Here's a Python script that uses a dictionary to map words to numbers, and then sorts them accordingly.

```python
from typing import Dict

# Dictionary to map words to numbers
num_dict: Dict[str, int] = {
    'zero': 0, 'one': 1, 'two': 2, 'three': 3, 'four': 4,
    'five': 5,'six': 6,'seven': 7, 'eight': 8, 'nine': 9
}

def sort_numbers(numbers: str) -> str:
    """
    Sort a space-delimited string of numbers from 'zero' to 'nine' from smallest to largest.

    Args:
    numbers (str): A space-delimited string of numbers from 'zero' to 'nine'.

    Returns:
    str: The string with numbers sorted from smallest to largest.
    """
    # Split the input string into a list of numbers
    num_list: List[str] = numbers.split()

    # Sort the list of numbers based on their numerical value
    sorted_num_list: List[str] = sorted(num_list, key=lambda x: num_dict[x])

    # Join the sorted list of numbers back into a string
    sorted_numbers: str =''.join(sorted_num_list)

    return sorted_numbers

# Example usage
if __name__ == "__main__":
    print(sort_numbers('three one five'))  # Output: one three five
    print(sort_numbers('nine eight seven'))  # Output: seven eight nine
```

This script defines a dictionary to map words to numbers, then uses the built-in `sorted` function to sort the list of numbers based on their numerical value. Finally, it joins the sorted list of numbers back into a string and returns the result.