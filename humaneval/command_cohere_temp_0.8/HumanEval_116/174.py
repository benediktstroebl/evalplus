```python
def count_ones(n):
    return bin(n).count('1')

def sort_array(arr):
    arr.sort(key=lambda n: (count_ones(n), -n))
    return arr
```

This Python script solves the problem by using a key function to create a custom sorting strategy for the list `arr`. In this case, the key function assigns a priority to each element `n` in the list `arr` by returning a tuple `(count_ones(n), -n)`. Here's how it works:

1. `count_ones(n)`: This helper function counts the number of occurrences of the digit '1' in the binary representation of the number `n`. For example, if `n` is 5, which is 101 in binary, this function will return 2. 
2. The first element in the key function's return value, `count_ones(n)`, sorts the list based on the number of ones in the binary representation. This ensures that in the resulting sorted list, elements with fewer ones come first, and elements with the same number of ones are sorted based on the second criterion. 
3. `-n` as the second element in the key function's return value indicates that the sorting algorithm should use the decimal value of `n` as a secondary criterion when two elements have an equal number of ones in their binary representation. The negative sign is essential for a descending decimal sort. 

The resulting sorted list meets the expectations outlined in the problem statement and is returned by the `sort_array` function.