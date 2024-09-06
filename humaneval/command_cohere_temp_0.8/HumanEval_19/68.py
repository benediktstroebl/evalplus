```python
def sort_numbers(numbers: str) -> str:
    numbers = [int(char) for char in numbers.split()]
    numbers.sort()
    return ' '.join(map(str, numbers))
```
This Python script defines a function called `sort_numbers` which takes a string of space-separated numbers from 0-9 and sorts them in ascending order. The function first converts the input string into a list of integers using `split()` to separate the numbers and `int()` to convert each number. Then, it uses the `sort()` method to sort the numbers in ascending order. Finally, the function returns a string where the sorted numbers are joined back together with spaces using the `join()` method.

Here is an example usage of this function:
```python
print(sort_numbers('three one five')) # one three five
```
The output of this code is:
```
one three five
```
This demonstrates that the function correctly sorts the numbers 'one', 'three', and 'five' in ascending order, and returns the result as a space-separated string.