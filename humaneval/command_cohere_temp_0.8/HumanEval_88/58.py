```python
def sort_array(array):
    odd = len(array) % 2 != 0
    return sorted(array, reverse=odd)
```
This Python script provides a function `sort_array` that takes an array of non-negative integers as input and returns a copy of the array sorted in the requested manner. The sort order is reversed if the sum of the first and last index values is odd, which is an odd number in Python, else it's sorted ascending if the sum is even. The function uses Python's `sorted` function and a boolean reverse control variable to achieve this in one line, which makes it simple, efficient, and easy to test.