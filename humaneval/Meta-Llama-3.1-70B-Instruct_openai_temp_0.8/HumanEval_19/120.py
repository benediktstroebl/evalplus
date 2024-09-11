```python
from typing import List, Dict

def sort_numbers(numbers: str) -> str:
    """
    Input is a space-delimited string of numberals from 'zero' to 'nine'.
    Valid choices are 'zero', 'one', 'two', 'three', 'four', 'five','six','seven', 'eight' and 'nine'.
    Return the string with numbers sorted from smallest to largest

    >>> sort_numbers('three one five')
    'one three five'
    """

    # Mapping of number words to their corresponding integer values
    number_mapping: Dict[str, int] = {
        'zero': 0, 'one': 1, 'two': 2, 'three': 3, 'four': 4,
        'five': 5,'six': 6,'seven': 7, 'eight': 8, 'nine': 9
    }

    # Split the input string into a list of number words
    number_words: List[str] = numbers.split()

    # Validate the input and convert the number words to their integer values
    try:
        numbers_to_sort: List[int] = [number_mapping[word] for word in number_words]
    except KeyError:
        raise ValueError("Invalid number word in input string")

    # Sort the integer values
    sorted_numbers: List[int] = sorted(numbers_to_sort)

    # Convert the sorted integer values back to number words
    sorted_number_words: List[str] = [word for word, number in number_mapping.items() if number in sorted_numbers]

    # Join the sorted number words into a string and return the result
    return''.join(sorted_number_words)


# Test the function
print(sort_numbers('three one five'))  # Output: 'one three five'
```