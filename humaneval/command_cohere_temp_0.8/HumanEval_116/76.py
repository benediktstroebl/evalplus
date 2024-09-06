```python
def count_ones(n):
    return bin(n).count('1')

def sort_array(arr):
    arr.sort(key=lambda n: (count_ones(n), -n))
    return arr
```

This code defines a `count_ones` function that calculates the number of ones in a given number's binary representation. It also defines the `sort_array` function, which sorts the given array using a custom sorting key. This key first compares the count of ones in the binary representation of numbers and sorts them in ascending order. If the number of ones is the same, it sorts the numbers in descending order based on their decimal value. The function returns the sorted array.