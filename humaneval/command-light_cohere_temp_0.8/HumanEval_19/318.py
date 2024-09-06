Here is a self-contained Python script that includes a function `sort_numbers`, which sorts a list of numbers in markdown style:
```python
from typing import List
def sort_numbers(numbers: List[int]) -> List[str]:
    """ Input is a list of numbers in any order.
    Convert numbers to strings and sort them, then convert back.
    Return a list of sorted strings
    """
    numbers = [str(num) for num in numbers]
    return sorted(numbers)
``` 
The above code converts a list of numbers into a list of strings, sorts them, and then converts them back into a list of numbers. The final output is a list of strings in ascending order.