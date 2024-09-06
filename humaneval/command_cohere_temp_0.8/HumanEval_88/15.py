```python
def sort_array(array):
    odd, even = array[:1] + array[-1:], array[1:-1]
    return odd if sum(odd) % 2 else even
```

This code divides the array into two distinct parts:
1. The first element (index = 0) and the last element (index = len(array) - 1). These are stored in the `odd` list.
2. All other elements (excluding the first and last) are stored in the `even` list.

Then, depending on whether the sum of the values in the `odd` list is odd or even, it returns either `odd` or `even`. 

This division allows the sort to be performed efficiently using list operations.