```python
def sort_array(array):
    odd, even = array[:1], array[-1:]
    return odd + even if sum(array[:1], array[-1:]) % 2 else even + odd
```
The script utilizes array slicing to divide the input array into two sub-arrays: `odd` (first element) and `even` (`last` element). Utilizing the ternary operator, it then determines whether the sum of the first and last elements should sort in ascending (`odd + even`) or descending (`even + odd`) order. The desired sort is then returned. 

This approach does not modify the original array, as stipulated by the prompt. It also has a linear time complexity of O(n), where n is the length of the input array.