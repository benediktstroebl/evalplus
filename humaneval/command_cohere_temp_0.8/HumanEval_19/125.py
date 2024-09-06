```python
from typing import List

def sort_numbers(numbers: str) -> str:
    numbers = [num for num in numbers.split()]
    numbers.sort()
    return ' '.join(numbers)
```
This Python script defines a function called `sort_numbers` which takes a string containing a space-delimited list of numbers from 'zero' to 'nine' as input. The function splits this input string into a list of individual numbers, sorts that list in ascending order, and then joins the sorted numbers back into a single string. The result is a string containing the numbers sorted from smallest to largest.