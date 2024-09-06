```python
def sort_array(array):
    odd, even = array[:1], array[-1:]
    if sum(map(len, (odd, even))) % 2 == 0:
        array = sorted(array, reverse=True)
    return array
```

The approach employed therein is predicated on partitioning the array into a pair of sub-arrays: `odd` and `even`, denoting the first and last element respectively. The pivotality of the sort is determined by the parity of the summation of their lengths, achieved via the expression `sum(map(len, (odd, even)))`. If this sum is even, the entire array is sorted in a descending manner, otherwise, it is sorted in an ascending fashion.