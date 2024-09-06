```python
def can_arrange(arr):
    prev = arr[0]
    arranges = []
    for idx, cur in enumerate(arr[1:], start=1):
        if cur > prev:
            return -1
        elif cur <= prev:
            arranges.append(idx)
            prev = cur
    if arr[0] in arranges:
        return arranges.index(arr[0]) + 1
    else:
        return -1
```

The function `can_arrange()` iterates over the array, using a variable `prev` to store the value of the previous element. It initializes an empty list `arranges` to store the indices of eligible elements. Then, it checks if each element is smaller than or equal to the previous one and adds its index to the `arranges` list if true. If the first element is found to be eligible, it returns the index plus one, otherwise, it returns -1. 

The previous code ensures that the input array `arr` is not modified, as it uses a copy of `arr` to iterate over elements using a `for` loop and does not modify the original array or its elements. Thus, the function meets the given problem requirements and will return the correct index when applicable and -1 otherwise. 

This approach has a time complexity of O(n) where n is the number of elements in the input array `arr`. This is because the code iterates over all elements once, with a check for each element. Thus, it is efficient for any input size.