```python
from typing import List

def sort_numbers(input_numbers: str) -> str:
    """ Input is a space-delimited string of numberals from 'zero' to 'nine'.
    Valid choices are 'zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight' and 'nine'.
    Return the string with numbers sorted from smallest to largest.
    """
    numbers = input_numbers.split()
    sorted_numbers = 'zero' if numbers[0] != 'zero' else ''

    for i in range(len(numbers)):
        for j in range(i + 1, len(numbers)):
            if numbers[i] > numbers[j]:
                numbers[i], numbers[j] = numbers[j], numbers[i]
                if i == j:
                    sorted_numbers += numbers[i]
                else:
                    sorted_numbers += ' ' + numbers[i]

    return sorted_numbers
```

This script takes a string of space-separated numbers from the given set of choices and returns a sorted string. The sorting algorithm used is a basic bubble sort. The `List` type is imported from the `typing` module to establish the expected type of the input parameter, however, please note that the code will work even without this declaration.

This problem can also be solved using more efficient algorithms and with a different approach, so if you are interested in other sorted algorithms, we can discuss their implementation.