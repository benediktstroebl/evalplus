```python
from typing import List

def sort_numbers(numbers: str) -> str:
    numbers = [char.lower() for char in numbers]
    sorted_numbers = ' '.join(sorted(numbers))
    return sorted_numbers
```

This Python script provides a function that takes a string of numbers and returns a new string with these numbers sorted in ascending order. The function converts the input string into a list of the lowercase numbers, sorts this list, and then joins the numbers back into a string.

For better readability, the numbers in the input string are converted to lowercase, so that 'One' is treated the same as 'one'. Also, the function assumes that there are no delimiters between the numbers in the input string. If there are spaces or other characters between numbers, these will be ignored when the numbers are split into a list.

The function's type annotation of `List[str]` for the parameter `numbers` indicates that the function expects a list of string inputs. This allows for applying appropriate typing checks when utilizing the function. 

This solution assumes that the input string contains only single-digit numbers and ignores any characters that aren't valid numbers from 'zero' to 'nine'. If you have a different set of valid numbers, you may need to adjust the parsing of the input string.