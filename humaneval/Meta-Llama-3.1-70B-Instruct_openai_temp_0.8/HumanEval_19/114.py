```python
from typing import List

# Define a dictionary that maps word representations of numbers to their integer equivalents
number_map = {
    'zero': 0, 'one': 1, 'two': 2, 'three': 3, 'four': 4,
    'five': 5,'six': 6,'seven': 7, 'eight': 8, 'nine': 9
}

def sort_numbers(numbers: str) -> str:
    """
    Sorts a space-delimited string of number words in ascending order.

    Args:
    numbers (str): A string containing space-delimited number words.

    Returns:
    str: A string containing the sorted number words.

    Raises:
    ValueError: If the input string contains invalid number words.
    """
    # Split the input string into a list of number words
    num_list = numbers.split()

    # Validate the input and convert the number words to integers
    try:
        num_ints = [number_map[num] for num in num_list]
    except KeyError as e:
        raise ValueError(f"Invalid number word: {e}")

    # Sort the list of integers
    num_ints.sort()

    # Convert the sorted integers back to number words
    sorted_num_list = [key for key, value in number_map.items() if value in num_ints]

    # Join the sorted number words into a string
    sorted_numbers =''.join(sorted_num_list)

    return sorted_numbers

# Example usage:
print(sort_numbers('three one five'))  # Output: 'one three five'
```