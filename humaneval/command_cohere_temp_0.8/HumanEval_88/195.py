```python
def sort_array(array):
    odd, even = False, False
    sum_ = sum(array[:2])
    if sum_%2 == 0:
        even = True
    else:
        odd = True
    if odd:
        array[:] = sorted(array)
    if even:
        array[:] = sorted(array, reverse=True)
    return array
```

The function initially determines whether the sum of the array's first two elements is even or odd. If the result is even, the array will be sorted in descending order, whereas an odd result indicates that the array will be sorted in ascending order.

The `sorted` function is then used to sort the array, but with a twist: `sorted(array, reverse=True)` sorts the array in descending order, whereas `sorted(array)` sorts it in ascending order. Finally, the function modifies the original array, guaranteeing that the problem's rule is followed and the original array is not modified.