```python
def count_ones(n):
    return bin(n).count('1')

def sort_array(arr):
    arr.sort(key=lambda n: (count_ones(n), -n))
    return arr
```

The `count_ones` helper function calculates the number of ones in the binary representation of each number in the array, and the `sort_array` function uses a custom key when sorting the array, first sorting by the count of ones in the binary representation and then by the absolute value of the number to break ties. The resulting sorted array meets the specified requirements. You can directly use this code to solve the problem.