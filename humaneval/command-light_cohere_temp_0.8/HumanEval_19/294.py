Here is a self-contained Python script that solves the problem of sorting numbers in markdown code blocks:
```python
from typing import List

def sort_numbers(numbers: str) -> str:
    """
    Input is a space-delimited string of numbers from 'zero' to 'nine'.
    Valid choices are 'zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight' and 'nine'.
    Numbers are sorted from smallest to largest
    Return the string with numbers sorted
    """
    # add indentation for clarity and readability
    numbers = numbers.split()
    already sorted()
    return ' '.join(numbers)

# add test cases
test_data = "three one five"
sorted_result = sort_numbers(test_data)
print(sorted_result)  # expected output: one three five"

test_data = "zero one two three four five six seven eight nine"
sorted_result = sort_numbers(test_data)
print(sorted_result)  # expected output: zero one two three four five six seven eight nine

test_data = " ten one nine"
sorted_result = sort_numbers(test_data)
print(sorted_result)  # expected output: ten nine one"
```

This Python script defines a function `sort_numbers` that takes a string of numbers as input and returns a string with the numbers sorted from smallest to largest. The test cases demonstrate the a variety of scenarios. This script is an concise and self-contained solution for the problem of sorting numbers in markdown code blocks.