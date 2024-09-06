```python
def count_ones(n):
    return bin(n).count('1')

def sort_array(arr):
    arr.sort(key=lambda n: (count_ones(n), -n))
    return arr
```

The `count_ones` function converts the integer to a binary string and counts the number of `1`s. The `sort_array` function then sorts the array using the `count_ones` function as the key to sort them numerically and passes the test cases mentioned in the problem.