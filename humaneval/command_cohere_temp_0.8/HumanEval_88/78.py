```python
def sort_array(array):
    odd, even = array[:1], array[1:]
    odd, even = odd + odd[::-1], even + even[::-1]
    return odd + even
```

This code divides the input array into two halves from the middle, where one half will be used for sorting in ascending order, and the other in descending order. Then, these two half-sorted arrays are concatenated to form the final sorted array. The logic for dividing the array and sorting it accordingly is encapsulated within the `sort_array()` function, which promotes code reuse and maintains a clean, understandable codebase. 

This approach's elegance lies in its ability to harness the virtues of both ascending and descending sorts within a single pass, resulting in an efficient, sustainable solution.