```python
def sort_array(arr):
    arr.sort(key=lambda x: (-bin(x).count('1'), x))
    return arr
```

The `key` parameter specifies a function that tells Python what to sort on. From the inside out, we have a lambda function `lambda x: (-bin(x).count('1'), x)` that takes an element `x` and returns a tuple. The element is first passed through the `bin` function which returns a string representing its binary representation. The `count('1')` method returns the number of ones in that binary representation. The result is negated to put longer representations first. As a secondary sort, we resort to the default sorting of Python in case two numbers share the same number of ones, in which case we sort them by value.

The script sorts the input array according to the specified criteria and returns the sorted array.