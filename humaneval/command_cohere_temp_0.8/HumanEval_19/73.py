```python
def sort_numbers(numbers: str) -> str:
    numbers = [int(char) for char in numbers.split()]
    numbers.sort()
    return ' '.join(map(str, numbers))
```
This Python script defines a function called `sort_numbers` which takes a string parameter called `numbers`. The function first splits the string into a list of numbers, then sorts the list in ascending order, and finally joins the sorted list back into a string. This is achieved using the following steps:
- `numbers = [int(char) for char in numbers.split()]`: This line transforms the space-delimited string of numbers into a list of integers.
- `numbers.sort()`: This line sorts the list of integers in ascending order.
- `return ' '.join(map(str, numbers))`: This line joins the sorted list of integers back into a string, using spaces as separators. 

The expected output for the provided test case is:
```bash
one three five
```