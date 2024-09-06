```python
def prod_signs(arr):
    result = None
    if arr:
        result = sum(x * y for x, y in zip(arr, arr[1:]))
    return result
```
This function uses a list comprehension with a zipper to multiply each number in the list by the following number's sign, and then sums the results. The zipper iterates over two iterables, in this case, slices of the input list, alternatively accessing elements at corresponding positions. The result is then returned. This solution is concise and efficient, with a time complexity of O(n). It avoids unnecessary complexity by utilizing the zipper technique to iterate over pairs of elements.