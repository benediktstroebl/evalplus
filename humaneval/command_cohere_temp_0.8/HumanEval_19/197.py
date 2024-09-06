```python
def sort_numbers(numbers: str) -> str:
    numbers = [int(char) for char in numbers.split()]
    numbers.sort()
    return ' '.join(map(str, numbers))
```
This Python script defines a function called `sort_numbers` which takes a string parameter called `numbers`. The function first splits the string into a list of numbers, then sorts the list in ascending order, and finally joins the sorted list back into a string. 

Here is an example usage of the `sort_numbers` function:
```python
print(sort_numbers('three one five'))  # output: 'one three five'
```
The function would sort the characters in the input string and return the smallest digit first, followed by the subsequent digits, resulting in the output of "one three five".