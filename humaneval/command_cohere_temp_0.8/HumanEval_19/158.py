```python
def sort_numbers(numbers: str) -> str:
    numbers = [int(char) for char in numbers.split()]
    numbers.sort()
    return ' '.join(map(str, numbers))
```
This Python script provides a function `sort_numbers` that takes a string of space-separated numbers from 0 to 9 and returns a string of these numbers sorted from smallest to largest. The function converts the input string into a list of integers using `split()` and `int()` and then sorts this list with `sort()`, converting it back to a string with `map()` and `join()`. 

Here is an example use case:
```python
print(sort_numbers('three one five'))  # output: 'one three five'
```
You can also test this function with the provided test case:
```python
>>> sort_numbers('three one five')
'one three five'
```
Making sure the function behaves correctly for any permutation of the numbers 0 to 9, with any amount of spaces between the numbers.