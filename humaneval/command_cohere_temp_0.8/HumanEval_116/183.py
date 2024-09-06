```python
def count_ones(n):
    return bin(n).count('1')

def sort_array(arr):
    arr.sort(key=lambda n: (count_ones(n), -n))
    return arr
```

The `count_ones` function counts the number of ones in the binary representation of a given number. The `sort_array` function uses a lambda to sort the array using the `count_ones` function as the key to sort them in ascending order based on the number of ones in their binary representation. For numbers with a similar number of ones, they are further sorted in descending order based on their decimal value. The function then returns the sorted array.