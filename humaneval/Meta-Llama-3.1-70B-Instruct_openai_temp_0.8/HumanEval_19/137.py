```python
from typing import List

def sort_numbers(numbers: str) -> str:
    """ Input is a space-delimited string of numberals from 'zero' to 'nine'.
    Valid choices are 'zero', 'one', 'two', 'three', 'four', 'five','six','seven', 'eight' and 'nine'.
    Return the string with numbers sorted from smallest to largest
    >>> sort_numbers('three one five')
    'one three five'
    """
    # Define a mapping of numeral words to their integer values
    numeral_map: dict[str, int] = {
        'zero': 0, 'one': 1, 'two': 2, 'three': 3, 'four': 4,
        'five': 5,'six': 6,'seven': 7, 'eight': 8, 'nine': 9
    }

    # Split the input string into a list of numeral words
    numeral_words: List[str] = numbers.split()

    # Sort the list of numeral words based on their integer values
    sorted_numerals: List[str] = sorted(numeral_words, key=numeral_map.get)

    # Join the sorted list of numeral words back into a string
    sorted_string: str =''.join(sorted_numerals)

    return sorted_string


# Example usage:
print(sort_numbers('three one five'))  # Output: 'one three five'
```