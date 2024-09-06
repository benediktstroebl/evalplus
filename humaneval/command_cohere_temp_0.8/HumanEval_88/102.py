```python
def sort_array(array):
    odd = len(array) % 2
    if odd:
        array[:] = sorted(array)
    else:
        array[:] = sorted(array, reverse=True)
```

This code provides a function called `sort_array` which takes a list called `array` as input. The function uses the modulo operator to check if the length of the array is odd by dividing it by 2 and using the remainder. If the length of the array is odd, the list is sorted using the `sorted` function. If the length of the array is even, the list is sorted in descending order using the `sorted` function and the `reverse=True` argument. The function uses the `*:` operator to modify the list in place.