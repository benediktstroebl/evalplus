```python
def sort_array(arr):
    arr.sort(key=lambda x: (bin(x).count('1'), x))
    return arr
```

The `key` argument in the `sort` method is used to specify a function that tells the sorting function how to compare each pair of elements. This lambda function takes the element `x`, counts the number of `1`s in its binary representation using `bin(x).count('1')`, and returns this count as a tuple together with the element itself. Elements with more `1`s in their binary representation will be sorted first, and if the number of `1`s is the same, they will be sorted based on their numerical value in decimal notation.