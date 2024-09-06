```python
def sort_array(arr):
    arr.sort(key=lambda x: (bin(x).count('1'), x))
    return arr
```

The `key` argument in the `sort` function is used to specify a function that defines the sort order. In this case, the function `lambda x: (bin(x).count('1'), x)` returns a tuple where the first element counts the number of `1`s in the binary representation of `x`, and the second element is `x` itself. This ensures that the sorting is done based on the number of `1`s in the binary representation when the first element is the same. The code then returns the sorted array `arr`. 

This code block solves the problem by sorting the array according to the number of ones in their binary representation and decimal value when the number of ones is the same. It returns the sorted array, which satisfies the given constraints.