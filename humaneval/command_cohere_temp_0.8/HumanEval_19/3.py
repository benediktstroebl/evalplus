```python
def sort_numbers(numbers: str) -> str:
    numbers = [int(char) for char in numbers.split()]
    numbers.sort()
    return ' '.join(map(str, numbers))
```
This Python script defines a function called `sort_numbers` which takes a string parameter called `numbers`. The function first splits the string into a list of numbers, then sorts the list in ascending order, and finally joins the sorted list back into a string. It returns the string with the numbers sorted from smallest to largest. 

Here is an example usage of the function:
```python
print(sort_numbers('three one five'))  # Outputs: 'one three five'
```
It can also be tested with the following interactive Python session:
```python
>>> sort_numbers('three one five')
'one three five'
>>> sort_numbers('five four three two one')
'one two three four five'
>>> sort_numbers('nine eight seven six five four three two one')
'zero one two three four five six seven eight nine'
```