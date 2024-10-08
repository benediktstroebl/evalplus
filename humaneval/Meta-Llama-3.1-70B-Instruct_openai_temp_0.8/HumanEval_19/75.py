```python
from typing import List

def sort_numbers(numbers: str) -> str:
    """
    This function sorts a space-delimited string of number words from 'zero' to 'nine' in ascending order.

    Args:
    numbers (str): A string containing space-delimited number words.

    Returns:
    str: The input string with number words sorted from smallest to largest.
    """

    # Define a dictionary to map number words to their corresponding integer values
    num_dict = {
        'zero': 0, 'one': 1, 'two': 2, 'three': 3, 'four': 4,
        'five': 5,'six': 6,'seven': 7, 'eight': 8, 'nine': 9
    }

    # Split the input string into a list of number words
    num_list: List[str] = numbers.split()

    # Sort the list of number words based on their corresponding integer values
    num_list.sort(key=lambda x: num_dict[x])

    # Join the sorted list of number words back into a string separated by spaces
    sorted_nums: str =''.join(num_list)

    return sorted_nums


# Example usage:
print(sort_numbers('three one five'))  # Output: 'one three five'
print(sort_numbers('nine eight seven six five four three two one zero'))  # Output: 'zero one two three four five six seven eight nine'
```