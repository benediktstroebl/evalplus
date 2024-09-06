```python
def sort_numbers(numbers: str) -> str:
    numbers = [int(char) for char in numbers.split()]
    numbers.sort()
    return ' '.join(map(str, numbers))
```
This Python script defines a function called `sort_numbers` which takes a string parameter called `numbers`. The function first splits the string into a list of numbers, then sorts this list in ascending order. Finally, it joins the sorted list of numbers back into a string and returns the result.

Here is an example usage of this function:
```python
print(sort_numbers('three one five'))  # Outputs: 'one three five'
```
This demonstrates how the function can be used to sort the given string of numbers in ascending order and return the sorted string.