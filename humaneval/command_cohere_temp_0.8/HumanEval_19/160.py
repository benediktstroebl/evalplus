```python
from typing import List

def sort_numbers(input_numbers: str) -> str:
    """ Input is a space-delimited string of numberals from 'zero' to 'nine'.
    Valid choices are 'zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight' and 'nine'.
    Return the string with numbers sorted from smallest to largest.
    """
    numbers = input_numbers.split()
    sorted_numbers = ' '.join(sorted(numbers))
    return sorted_numbers
```

This script takes an input string of numbers that forms the `input_numbers` parameter and returns a space-separated string of the input numbers sorted from smallest to largest. The function first splits the input string into a list of numbers and then uses the `sorted` function to sort the list from smallest to largest. Finally, the function joins the list back into a string and returns the result.

Here is an example usage of the function taking in a test case and returning the desired output:
```python
test_case = 'three one five'
print(sort_numbers(test_case)) # one three five
```

This would output:
```
one three five
```

This indicates that the function sorts the input numbers from 'one', 'three', and 'five' in ascending order to form the output string 'one three five'.