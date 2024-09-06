```python
from typing import List

def sort_numbers(numbers: str) -> str:
    numbers = [int(char) for char in numbers.split()]
    numbers.sort()
    return ' '.join(map(str, numbers))
```
This Python script solves the problem using the following steps:
1. The `sort_numbers` function takes a string of space-separated numbers (`numbers`) as input.
2. It splits the input string into a list of characters, and then converts each character to its corresponding integer.
3. The list of integers is sorted in ascending order using the `sort()` method.
4. Finally, the sorted integers are converted back to a string and joined with spaces using the `join()` method.

This algorithm ensures that the input string of numbers is sorted correctly and returned as a string. The function is self-contained and easy to use, making it practical for solving this specific problem and others like it.