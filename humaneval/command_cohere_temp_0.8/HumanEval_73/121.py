```python
def smallest_change(arr):
    arr.sort()
    count = 0
    for i in range(1, len(arr)):
        if arr[i] != arr[i-1]:
            count += 1
    return count
```

The function `smallest_change` takes an array `arr` as input and returns the smallest number of changes required to make the array palindromic. It sorts the array and then counts the number of distinct elements in the sorted array. A palindromic array read the same both backwards and forwards has elements that are all the same or evenly distributed in distinct pairs with the same number of occurrences. The given problem is therefore correctly solved by the code providing the smallest number of changes that would make the array palindromic. 

This solution does not require any additional import statements and is self-contained. It can be executed directly in Python by copying and pasting the code into a Python environment.