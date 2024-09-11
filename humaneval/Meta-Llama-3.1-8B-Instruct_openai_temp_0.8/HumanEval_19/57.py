```python
from typing import List, Dict


def sort_numbers(numbers: str) -> str:
    """
    Input is a space-delimited string of numberals from 'zero' to 'nine'.
    Valid choices are 'zero', 'one', 'two', 'three', 'four', 'five','six','seven', 'eight' and 'nine'.
    Return the string with numbers sorted from smallest to largest

    Args:
        numbers (str): A space-delimited string of numberals.

    Returns:
        str: The sorted string.

    Example:
        >>> sort_numbers('three one five')
        'one three five'
    """
    # Define a dictionary with number words as keys and their integer values as values
    num_dict: Dict[str, int] = {
        'zero': 0, 'one': 1, 'two': 2, 'three': 3, 'four': 4,
        'five': 5,'six': 6,'seven': 7, 'eight': 8, 'nine': 9
    }

    # Split the input string into a list of words
    word_list: List[str] = numbers.split()

    # Sort the list based on the integer values in the dictionary
    sorted_list: List[str] = sorted(word_list, key=lambda x: num_dict[x])

    # Join the sorted list into a string separated by spaces
    sorted_string: str =''.join(sorted_list)

    return sorted_string


# Example usage
print(sort_numbers('three one five'))  # Output: 'one three five'
print(sort_numbers('nine eight seven'))  # Output:'seven eight nine'
print(sort_numbers('five four three two one'))  # Output: 'one two three four five'
```

In this script, we first define a dictionary `num_dict` that maps each number word to its corresponding integer value. We then use the `sorted` function with a custom sorting key (a lambda function that looks up the integer value in the dictionary) to sort the list of words. Finally, we join the sorted list into a string separated by spaces and return the result.