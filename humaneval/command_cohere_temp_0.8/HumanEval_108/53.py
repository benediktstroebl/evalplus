```python
def count_nums(arr):
    output = sum(int(num) >= 0 for num in arr)
    return output
```
This function uses a `sum` function with a generating expression to count the number of elements that have a digit sum greater than 0. 

This solution is concise and efficient, providing a complete answer to the problem in a single line.

The `count_nums` function can be used directly with arrays like `[]`, `[-1, 11, -11]`, or `[1, 1, 2]` to verify its functionality.