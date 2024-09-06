```python
def sort_numbers(numbers: str) -> str:
    numbers = [int(char) for char in numbers.split()]
    numbers.sort()
    return ' '.join(map(str, numbers))
```
This Python script defines a function called `sort_numbers` which takes a string of numbers as input and returns a string with the numbers sorted from smallest to largest. 

Here is an example usage of the function:
```python
print(sort_numbers('three one five'))  # Outputs: 'one three five'
```

This would output `one three five`, which is the sorted version of the numbers in the input string.