### Python Script to Sort Numbers in a String
```python
from typing import List

def sort_numbers(numbers: str) -> str:
    """
    Sorts a space-delimited string of numbers from 'zero' to 'nine' 
    from smallest to largest.

    Args:
        numbers (str): A space-delimited string of numbers.

    Returns:
        str: The sorted string of numbers.
    """
    # Split the input string into a list of words
    num_list: List[str] = numbers.split()

    # Create a dictionary to map words to their corresponding numerical values
    num_dict: dict[str, int] = {
        'zero': 0, 'one': 1, 'two': 2, 'three': 3, 'four': 4,
        'five': 5,'six': 6,'seven': 7, 'eight': 8, 'nine': 9
    }

    # Use the sorted function to sort the list of numbers
    sorted_list: List[str] = sorted(num_list, key=lambda x: num_dict[x])

    # Join the sorted list back into a string
    sorted_str: str =''.join(sorted_list)

    return sorted_str

# Example usage
print(sort_numbers('three one five'))  # Output: 'one three five'
print(sort_numbers('eight nine zero'))  # Output: 'zero eight nine'
```