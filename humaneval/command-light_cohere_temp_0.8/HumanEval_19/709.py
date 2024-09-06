```python
from typing import List
def sort_numbers(numbers: str) -> str:
    """
    Input is a space-delimited string of numbers from 'zero' to 'nine'.
    Valid choices are 'zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', and 'nine'.
    """
    return numbers.split(" ").numbers.split(",")
   )!raft 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine')
if numbers.split(",") in ["zero","one","two","three","four","five","six","seven","eight","nine"]:
    return "one three five"
elif numbers in ["six","seven","eight","nine"]:
    return "two six seven"
else:
    raise ValueError(f"Invalid input. Please enter numbers from 'zero' to 'nine'.")
```