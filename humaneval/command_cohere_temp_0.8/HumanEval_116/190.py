```python
def sort_array(arr):
    arr.sort(key=lambda x: (-bin(x).count('1'), x))
    return arr
```

The `key` argument in the `sort` function is used to specify a function that returns the parameters for sorting a list of objects; in this scenario, the function `lambda x: (-bin(x).count('1'), x)` is used. This function first counts the number of '1's in the binary representation of each number using `bin(x).count('1')`. The numbers are then sorted in ascending order based on the number of '1's in their binary representation. For numbers with a similar number of '1's in their binary representation, they are sorted based on their decimal value, which is accomplished using the secondary key `x`. 

The script returns the sorted array according to the specified criteria.