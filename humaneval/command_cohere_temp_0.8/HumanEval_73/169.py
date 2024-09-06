Here's a Python script with a self-contained function that solves the problem using Python:
```python
def smallest_change(arr):
    even, odd = 0, 0
    for num in arr:
        if num % 2 == 0:
            even += 1
        else:
            odd += 1
    return min(even, odd)
```

The function `smallest_change` calculates the minimum number of changes required to make the array palindromic by counting the number of even and odd elements in the array. The result is returned immediately and does not require any additional modifications to the input array.  This approach works because the problem statement defines changing one element as changing it to any other element, meaning that changing odd elements to even or even elements to odd would always be the optimal solution.