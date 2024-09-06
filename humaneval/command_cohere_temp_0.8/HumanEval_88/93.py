```python
def sort_array(array):
    odd = sum(array[0], array[-1]) % 2
    if odd:
        array[:] = sorted(array)
    else:
        array[:] = sorted(array, reverse=True)
    return array
```

The function sorts the array **in place** by using the **sorted()** function with a custom sorting key and the **reverse** parameter set to **True** if the sum of the first and last element of the array is even, otherwise it sorts the array in ascending order.