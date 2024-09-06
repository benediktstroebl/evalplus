```python
def count_ones(n):
    return bin(n).count('1')

def sort_array(arr):
    arr.sort(key=lambda n: (count_ones(n), -n))
    return arr
```

This script employs Python's `count_ones` function to tally the number of '1's in a number's binary representation. Subsequently, it utilizes Python's `sort_array` function to arrange the array according to this specified criterion. Notably, the algorithm sorts the array such that numbers with an equal count of '1's are sorted in descending order, thereby earning the descending '-' modifier in the `sort_array` function's lambda. This arrangement ensures that numbers with more '1's emerge before those with fewer.