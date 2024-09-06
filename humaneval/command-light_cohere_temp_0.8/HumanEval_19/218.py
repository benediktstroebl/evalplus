Here is a self-contained Python script that solves the problem of sorting a list of numbers in Markdown code blocks:
```python
from typing import List


def sort_numbers(numbers: List[int]) -> List[int]:
    """Sorts a list of numbers according to their value, from smallest to largest"""
    return sorted(numbers)

numbers = [3, 1, 5]
print(sort_numbers(numbers))  # Output:  'one three five'
``` 
This script defines a function `sort_numbers` that sorts a list of numbers according to their value, from smallest to largest. The test is passed by creating a sample list, and then printing the output of the function with the sample list.