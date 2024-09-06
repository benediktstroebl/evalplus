Here's a Python script with a self-contained function that solves the problem:
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
The function smallest_change calculates the minimum number of elements that need to be changed to make the array palindromic. It uses the increment variables even and odd to keep track of the number of even and odd elements in the array respectively. It then returns the smaller of the two counts, which is the minimum number of changes required.