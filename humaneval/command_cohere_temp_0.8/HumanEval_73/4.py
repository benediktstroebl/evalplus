```python
def smallest_change(arr):
    arr.sort()
    return sum(1 for i in range(len(arr)//2) if arr[i] != arr[-(i+1)])
```
The function `smallest_change()` works by first sorting the input array, which ensures that the array is palindromic if all elements are the same. Then, it iterates over the array's middle half and counts the number of elements that are not duplicated in the reverse order. This number represents the minimum changes required to make the array palindromic, as we only need to change the unique elements in the middle half to their corresponding reverse elements.