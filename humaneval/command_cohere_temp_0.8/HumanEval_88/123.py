```python
def sort_array(array):
    odd = sum(array[0], array[-1]) % 2
    if odd:
        array[:] = sorted(array)
    else:
        array[:] = sorted(array, reverse=True)
    return array
```

The function sorts the array as explained in the prompt and returns the sorted array. An array slice `array[:]` was used to sort the array in place to avoid returning a sorted copy that requires additional memory.