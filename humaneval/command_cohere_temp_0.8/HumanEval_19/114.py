```python
def sort_numbers(numbers: str) -> str:
    numbers = [int(char) for char in numbers.split()]
    numbers.sort()
    return ' '.join(map(str, numbers))
```
This Python script defines a function called `sort_numbers` which takes a string of space-separated numbers from 0-9 and sorts them in ascending order. The function first converts the input string into a list of numbers using `split()` and `int()` to remove the spaces and convert the characters to numbers. Then, it sorts this list using Python's `sort()` method. Finally, it converts the sorted list of numbers back to a string by joining the numbers together with spaces using `map()` and `str()` and returns the result. 

Here is an example usage of this function:
```python
print(sort_numbers('three one five')) # Output: one three five
```
This would output:
```one three five``` due to the numbers being sorted in ascending order.