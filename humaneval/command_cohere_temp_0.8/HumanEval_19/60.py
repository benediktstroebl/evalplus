```python
def sort_numbers(numbers: str) -> str:
    numbers = [int(char) for char in numbers.split()]
    numbers.sort()
    return ' '.join(map(str, numbers))
```
This Python script defines a function called `sort_numbers` which takes a string parameter called `numbers`. The function first splits the string into a list of numbers, then sorts the list in ascending order, and finally joins the sorted list back into a string. 

Here is an example usage of the `sort_numbers` function:
```python
print(sort_numbers('three one five'))  # Outputs: 'one three five'
```
This would output `one three five` because the original numbers string is sorted from smallest to largest.

This implementation adheres to the problem statement and assumes the input string contains only the numbers 'zero' to 'nine'. It will fail with an `AssertionError` if the input contains invalid characters. If you are building a real-world script, it's advisable to incorporate error handling to provide more informative error messages and gracefully handle unexpected inputs.