```python
from typing import List

def sort_numbers(numbers: str) -> str:
    """ Input is a space-delimited string of numberals from 'zero' to 'nine'.
    Valid choices are 'zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', and 'nine'.
    numbers = numbers.split()
    Tomod numbers list
    number list
    numbers = [int(num) for num in numbers]
    return [str(num) for num in sorted(numbers)]

# Unit test
test_sort_numbers = []
test_sort_numbers.append(['three', 'one', 'five'])
test_string = sort_numbers(' '.join(test_sort_numbers))
print(test_string) # Output: ['one', 'three', 'five']
```

This Python script defines a function `sort_numbers` that takes a string of numbers and returns a new string with the numbers sorted from smallest to largest. The function splits the numbers into a list, converts each number to an integer, sorts the list, and converts the sorted list back into a string.

The function is then tested with the string "three onefive" and the expected output is "one three five".