```python
def smallest_change(arr):
    arr = list(set(arr))
    return sum([1 for i in range(len(arr)) if arr[i] != arr[len(arr) - 1 - i]])
```

The function `smallest_change` works by first removing all duplicated elements in the input array using the `set()` method, which allows it to focus on the uniqueness of the elements. It then returns the sum of binary elements where the position of each element is checked against its mirror position in the reversed array, and if the element doesn't match its mirror image, the count increases by 1.

This approach ensures that the function can provide the minimum number of changes required to make the array palindromic, as per the problem definition.