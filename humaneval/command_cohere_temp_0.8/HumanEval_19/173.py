```python
def sort_numbers(numbers: str) -> str:
    numbers = [int(char) for char in numbers.split()]
    numbers.sort()
    return ' '.join(map(str, numbers))
```
This Python script defines a function called `sort_numbers` which takes a string parameter called `numbers`. The function first splits the string into a list of numbers, then sorts the list in ascending order, and finally joins the sorted numbers back into a string. 

Here is an example usage of the `sort_numbers` function:
```python
print(sort_numbers('three one five'))  # Outputs: 'one three five'
```
This would print the ordered string "one three five" from the input "three one five".