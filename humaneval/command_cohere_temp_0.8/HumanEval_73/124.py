Here's a Python script with a self-contained function that solves the problem:
```python
def smallest_change(arr):
    odd = sum(x%2 for x in arr)
    if odd % 2 == 1:
        return len(arr) // 2
    else:
        return len(arr) // 2 - 1

# Tests:
arr1 = [1,2,3,5,4,7,9,6]
assert smallest_change(arr1) == 4

arr2 = [1, 2, 3, 4, 3, 2, 2]
assert smallest_change(arr2) == 1

arr3 = [1, 2, 3, 2, 1]
assert smallest_change(arr3) == 0
```

The function `smallest_change` calculates the smallest number of changes needed to make the array palindromic. If the number of odd elements is odd, then the center two elements cannot be the same, so `len(arr) // 2` changes are needed. If the number of odd elements is even, then the center element is okay as it is, so `len(arr) // 2 - 1` changes are needed.