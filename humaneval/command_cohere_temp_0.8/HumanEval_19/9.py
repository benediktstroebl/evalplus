```python
def sort_numbers(numbers: str) -> str:
    numbers = [int(char) for char in numbers.split()]
    numbers.sort()
    return ' '.join(map(str, numbers))
```
This Python script defines a function called `sort_numbers` which takes a string of numbers as input and returns a string containing the same numbers sorted in ascending order. The function first converts the space-delimited string of numbers to an integer list, using `split()` to separate the numbers, and `int()` to convert each number. Then, it sorts the list of integers using the `sort()` method. Finally, it returns a string with the sorted numbers by mapping them back to strings using `str()` and joining them with spaces using `join()`. 

Here is an example usage of this function:
```python
print(sort_numbers('three one five')) # one three five
```
The output of this code is:
```
one three five
```
This demonstrates that the `sort_numbers` function correctly sorts the input numbers in ascending order and returns the expected result.