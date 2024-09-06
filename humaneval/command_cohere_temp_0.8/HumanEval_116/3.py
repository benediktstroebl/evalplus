```python
def count_ones(n):
    return bin(n).count('1')

def sort_array(arr):
    arr.sort(key=lambda n: (count_ones(n), -n))
    return arr
```

The code defines a Python function `sort_array` that sorts an array of non-negative integers according to the number of ones in their binary representation in ascending order. For integers with the same number of ones, it sorts based on the decimal value in descending order. The function uses the `count_ones` helper function to calculate the number of ones in the binary representation of each integer. The `sort` method is used with a custom key function that combines the count of ones and the decimal value in a tuple, ensuring the correct sorting order.