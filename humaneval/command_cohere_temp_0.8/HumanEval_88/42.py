```python
def sort_array(array):
    odd, even = False, False
    if sum(array[0], array[-1]) % 2 == 1:
        odd = True
    if sum(array[0], array[-1]) % 2 == 0:
        even = True
    if odd:
        array.sort()
    elif even:
        array.sort(reverse=True)
    return array
```

The provided Python script sorts an array of non-negative integers based on the sum of its first and last elements, following the problem statement's guidelines. It initially determines whether the sum is odd or even, then sorts the array in the appropriate order, either ascending or descending. This method effectively handles the situation and produces the desired sorted array.