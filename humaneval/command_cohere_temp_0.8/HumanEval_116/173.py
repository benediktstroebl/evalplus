```python
def sort_array(arr):
    arr.sort(key=lambda x: (-bin(x).count('1'), x))
    return arr
```

The `key` parameter of the `sort` method is used to specify a function that transforms each element in the list to a tuple of keys, in this case, we are using a lambda function `(-bin(x).count('1'), x)` to transform each element `x` to a tuple consisting of `(-bin(x).count('1'), x)`. 

`bin(x)` converts the integer `x` to a binary string representation, and `.count('1')` counts the number of occurrences of the character '1' in the binary representation of the element `x`, so the result is sorted in ascending order based on the number of ones in the binary representation of each number.

If the number of ones is the same, then it sorts based on the decimal value of the numbers.

This solution efficiently solves the problem and sorts the array as described in the prompt.