### Sorting Numbers in a String
```python
from typing import Dict

def sort_numbers(numbers: str) -> str:
    """
    Input is a space-delimited string of numerical words from 'zero' to 'nine'.
    Valid choices are 'zero', 'one', 'two', 'three', 'four', 'five','six','seven', 'eight', and 'nine'.
    Return the string with numbers sorted from smallest to largest.

    Args:
    numbers (str): A space-delimited string of numerical words.

    Returns:
    str: The string with numbers sorted from smallest to largest.
    """
    # Dictionary to map numerical words to their corresponding integer values
    num_dict: Dict[str, int] = {
        'zero': 0, 'one': 1, 'two': 2, 'three': 3, 'four': 4,
        'five': 5,'six': 6,'seven': 7, 'eight': 8, 'nine': 9
    }

    # Split the input string into a list of numerical words
    num_list: List[str] = numbers.split()

    # Create a list of tuples containing the numerical words and their corresponding integer values
    num_list_with_values: List[tuple] = [(num, num_dict[num]) for num in num_list]

    # Sort the list of tuples based on the integer values
    sorted_num_list: List[tuple] = sorted(num_list_with_values, key=lambda x: x[1])

    # Extract the numerical words from the sorted list of tuples
    sorted_num_list_str: List[str] = [num[0] for num in sorted_num_list]

    # Join the sorted list of numerical words into a string separated by spaces
    sorted_numbers: str =''.join(sorted_num_list_str)

    return sorted_numbers

# Example usage
print(sort_numbers('three one five'))  # Output: 'one three five'
```

This script defines a function `sort_numbers` that takes a space-delimited string of numerical words as input, sorts them based on their integer values, and returns the sorted string. The example usage demonstrates how to call the function with the input string `'three one five'` and print the sorted output.