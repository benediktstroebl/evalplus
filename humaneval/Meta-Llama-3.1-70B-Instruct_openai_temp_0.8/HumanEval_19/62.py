```python
from typing import List

def sort_numbers(numbers: str) -> str:
    """
    Sorts a space-delimited string of numberals from 'zero' to 'nine' in ascending order.

    Args:
        numbers (str): A space-delimited string of numberals.

    Returns:
        str: The input string with numbers sorted from smallest to largest.

    >>> sort_numbers('three one five')
    'one three five'
    """

    # Define a dictionary to map number words to their corresponding integer values
    num_dict = {
        'zero': 0, 'one': 1, 'two': 2, 'three': 3, 'four': 4,
        'five': 5,'six': 6,'seven': 7, 'eight': 8, 'nine': 9
    }

    # Split the input string into a list of number words
    num_list = numbers.split()

    # Sort the list of number words based on their corresponding integer values
    sorted_num_list = sorted(num_list, key=lambda x: num_dict[x])

    # Join the sorted list of number words back into a string
    sorted_numbers =''.join(sorted_num_list)

    return sorted_numbers


# Example usage
if __name__ == "__main__":
    numbers = 'three one five'
    print(sort_numbers(numbers))  # Output: 'one three five'
```