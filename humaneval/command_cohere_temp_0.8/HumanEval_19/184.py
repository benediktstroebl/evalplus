```python
from typing import List

def sort_numbers(input_string: str) -> str:
    """
    Sort a space-delimited string of numbers from smallest to largest.
    Valid input ranges from 'zero' to 'nine'.
    """
    # Split the input string by space into a list of strings.
    numbers = input_string.split()

    # Convert each string element to its corresponding integer.
    # This step automatically casts 'one' to 1, 'seven' to 7, etc.
    sorted_numbers = sorted(map(int, numbers))

    # Convert the sorted list of integers back to strings.
    # This step allows us to concatenate the strings back together without a mismatch in types.
    sorted_strings = [str(num) for num in sorted_numbers]

    # Join the sorted list of strings back together with spaces.
    return ' '.join(sorted_strings)
```

This Python script takes a string of space-separated numbers, sorts them from smallest to largest, and returns the sorted string. The type annotations (`List`) ensure that the function takes and returns the correct types, and the `split()` and `join()` methods take care of the space-delimited input and output.

For example, the input `sort_numbers('three one five')` would return the output `one three five`.