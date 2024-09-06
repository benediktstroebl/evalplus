```python
def count_ones(n):
    return bin(n).count('1')

def sort_array(arr):
    arr.sort(key=lambda n: (count_ones(n), -n))
    return arr
```

This code defines a `count_ones` function that calculates the number of ones in a given number's binary representation. It also defines the `sort_array` function, which sorts the given array using a custom sorting key. This key is a lambda function that returns a tuple, with the first element being the result of the `count_ones` function and the second element being the absolute value of the number. This ensures that numbers with the same number of ones in their binary representation are sorted in descending order. Once the array is sorted, it is returned.