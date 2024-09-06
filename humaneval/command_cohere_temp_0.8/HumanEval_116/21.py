```python
def count_ones(n):
    return bin(n).count('1')

def sort_array(arr):
    arr.sort(key=lambda n: (count_ones(n), -n))
    return arr
```

The code defines a Python function `sort_array` that sorts an array of non-negative integers according to the number of ones in their binary representation. It uses a custom sorting key that first compares elements based on their binary ones count in ascending order and then, for elements with the same number of ones, sorts them in descending order based on their decimal value. The function retains the intended behavior specified in the problem statement and should work correctly for the given test cases.