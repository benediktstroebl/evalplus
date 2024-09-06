```python
def count_nums(arr):
    output = sum(int(num) >= 0 for num in arr)
    return output
```
This function uses a `sum` function with a generating expression to count the number of elements that have a digit sum greater than 0. 

This solution is concise and efficient, providing a complete answer to the problem in a single line.

The `count_nums` function should return:
- 0, if the list is empty;
- 1, if the list contains only one element (-1);
- 2, if the list contains two elements (-1, 11);
- 3, if the list contains three elements (-1, 11, -11).

This approach is based on the idea that a number has a positive digit sum if and only if it is non-negative. 

This is a powerful and versatile technique for solving problems involving iterables and conditions in Python.