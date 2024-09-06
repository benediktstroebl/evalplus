```python
def sort_array(array):
    odd, even = False, False
    if sum(array[0], array[-1]) % 2 == 0:
        even = True
    if sum(array[0], array[-1]) % 2 == 1:
        odd = True
    if odd:
        array.sort(reverse=False)
    if even:
        array.sort(reverse=True)
    return array
```

The script first checks if the sum of the first and last elements of the array is even, and sets a boolean variable `even` to `True`. If the sum is odd, then the variable `odd` is set to `True`.

The script then checks the value of the `odd` and `even` variables and sorts the array in the appropriate manner, using the `sort()` method and the `reverse` parameter. The array is sorted in ascending order when `odd` is `True`, and in descending order when `even` is `True`. Finally, the sorted array is returned. 

This solution is efficient and uses a low time complexity of `O(n log n)`, where `n` is the length of the array.