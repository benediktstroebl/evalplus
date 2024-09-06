```python
def sort_numbers(numbers: str) -> str:
    numbers = [int(char) for char in numbers.split()]
    numbers.sort()
    return ' '.join(map(str, numbers))
```
This Python script defines a function called `sort_numbers` which takes a string of numbers as input and returns a string with the numbers sorted from smallest to largest. 

The function first converts the space-delimited string of numbers into a list of integers. Then, it sorts this list in ascending order. Finally, it converts the sorted list of numbers back to a string by joining the list elements with spaces and returns the result. 

The function sorts the numbers numerically, not lexicographically, so '999' would appear sorted as '000', not '999'. 

This approach assumes that the input string contains only single-digit numbers and that each number is separated by exactly one space. If the input string has different spacing conventions or includes multi-digit numbers, the function may not work as intended.