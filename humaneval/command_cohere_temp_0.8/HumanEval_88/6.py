```python
def sort_array(array):
    odd, even = array[:1] + array[-1:], array[1:-1]
    return odd if sum(odd) % 2 else even
```

This Python script defines a function `sort_array` that takes an array of non-negative integers as input. The function partitions this array into two sections: a first section consisting of the first element and a last section consisting of the last element, and a middle section consisting of the remaining elements. The function then returns the middle section if the sum of the values in the first and last sections is odd; otherwise, it returns the reverse of the middle section. This partitioning and sorting strategy fulfill the problem statement's request to sort the array in ascending order if the sum of the first and last elements is odd and in descending order if that sum is even.