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
        str: The input string with numbers sorted from smallest to largest.
    """

    # Create a dictionary to map number words to their integer values
    num_map: Dict[str, int] = {
        'zero': 0, 'one': 1, 'two': 2, 'three': 3, 'four': 4,
        'five': 5,'six': 6,'seven': 7, 'eight': 8, 'nine': 9
    }

    # Split the input string into a list of number words
    num_words: List[str] = numbers.split()

    # Sort the list of number words based on their integer values
    sorted_num_words: List[str] = sorted(num_words, key=lambda word: num_map[word])

    # Join the sorted list of number words back into a string
    sorted_numbers: str =''.join(sorted_num_words)

    return sorted_numbers


# Test the function
print(sort_numbers('three one five'))  # Output: 'one three five'
```

This script works by first mapping the number words to their integer values, then sorting the list of number words based on these values. Finally, it joins the sorted list back into a string, which is then returned as the result.