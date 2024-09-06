```python
def count_ones(n):
    return bin(n).count('1')

def sort_array(arr):
    arr.sort(key=lambda n: (count_ones(n), -n))
    return arr
```

The `count_ones` helper function calculates the number of occurrences of 1 in the binary representation of each number in the array, which is used as a basis for sorting. The `sort_array` function uses the `count_ones` as the sorting key, first sorting the array based on the count of ones in the binary representation in ascending order. If the number of ones is the same for two or more numbers, it sorts them based on their decimal value in descending order.