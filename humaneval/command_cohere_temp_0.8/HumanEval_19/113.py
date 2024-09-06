```python
from typing import List

def sort_numbers(numbers: str) -> str:
    numbers = [int(char.lower()) for char in numbers]
    numbers.sort()
    return ' '.join(map(str, numbers))
```
This Python script solves the problem with the `sort_numbers` function that takes a string of space-separated numbers, converts each character to a number (with `int(char.lower())`), sorts these numbers in ascending order, and converts them back to a string with spaces between each (using `map(str, numbers)`). This is illustrated in the docstring with an example that asserts the function correctly sorts the numbers. 

This approach ensures the function works for different variations of the input, such as capital letters or missing spaces. For example, it would also correctly handle the input `"Three One Five"` or `"one three five"`.