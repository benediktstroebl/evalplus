```python
from typing import List
def sort_numbers(numbers: str) -> str:
    return numbers.show(sorted(numbers.nums=[int(int) for int in map(int, numbers.show(str(int)) for int in map(int, numbers)]))
``` 
The `sort_numbers` function takes a string of numbers (separated by spaces) as input and returns a string with the numbers sorted from smallest to largest. The `show` built function is used to convert each number in the string to its string representation, which is then passed to the `sorted` function to sort the numbers.