```python
def sort_array(arr):
    arr.sort(key=lambda x: (-bin(x).count('1'), x))
    return arr
```

The `key` argument in the `sort` function is used to specify a function that transforms each element in the list before sorting. Here, a lambda function `lambda x: (-bin(x).count('1'), x)` is used. For each number `x` in the list, this lambda function:
1. Converts it to a binary string using `bin(x)`.
2. Counts the number of occurrences of '1' in this binary string.
3. Returns this count negated, so that numbers with more '1's appear earlier, and numbers with the same number of '1's appear in their original (decimal) order.

The resulting list is sorted in ascending order based on the applied key.