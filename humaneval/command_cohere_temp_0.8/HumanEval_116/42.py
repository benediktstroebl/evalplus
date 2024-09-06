```python
def sort_array(arr):
    arr.sort(key=lambda x: (bin(x).count('1'), x))
    return arr
```

The `key` argument in the `sort` method is used to specify a function that describes the logic of how the sorting happens. In this case, for every element `x` in the array, the key function returns a tuple `(bin(x).count('1'), x)`, where `bin(x)` gives the binary representation of number `x`, and `.count('1')` counts the number of ones in that binary representation. When sorting based on the number of ones in the binary representation, the output of the key function is `(3, 4)` for `4` and `(2, 2)` for `2`, and `[4, 2]` will be the resulting array. Finally, the sorted array according to the described logic is obtained.