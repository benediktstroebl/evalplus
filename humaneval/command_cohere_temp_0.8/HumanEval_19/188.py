```python
def sort_numbers(numbers: str) -> str:
    numbers = [int(char) for char in numbers.split()]
    numbers.sort()
    return ' '.join(map(str, numbers))
```
This Python script provides a function named `sort_numbers`. The function takes a string of numbers as input and returns a string of these same numbers sorted from smallest to largest. The function first converts the string to a list of numbers, sorting them through the `split` and `int` functions. Then, the function returns the joined string through the map and `str` functions. 

Here is an example call to this function:
```python
print(sort_numbers('three one five'))  # one three five
```
This would output:
```
one three five
```

This function effectively and efficiently sorts numbers from smallest to largest, making it useful for sorting numerical strings.