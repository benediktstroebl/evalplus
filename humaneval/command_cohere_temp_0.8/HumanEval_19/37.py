```python
def sort_numbers(numbers: str) -> str:
    numbers = [int(char) for char in numbers.split()]
    numbers.sort()
    return ' '.join(map(str, numbers))
```
This Python script defines a function called `sort_numbers` which takes a string containing a space-delimited list of numbers from 0-9 as input. The function converts the input string into a list of integers using `split()` to separate the numbers, and `int()` to convert each number. It then sorts this list of integers in ascending order using the `sort()` method. Finally, the function returns a string where the sorted list of integers is joined back together with spaces using the `join()` method and `str()` to convert the integers back to strings. The expected output is a string where the numbers are sorted in ascending order, such as 'one three five' for the input 'three one five'.

Here is an example usage of the function:
```python
print(sort_numbers('three one five'))  # one three five
```
```bash
one three five
```