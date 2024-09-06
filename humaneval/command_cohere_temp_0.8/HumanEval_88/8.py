```python
def sort_array(array):
    odd = sum(array[0], array[-1]) % 2
    if odd:
        array[:] = sorted(array)
    else:
        array[:] = sorted(array, reverse=True)
```

The function sorts the array in ascending order if the sum of the first and last elements is odd, and in descending order if the sum is even.

This approach uses the `sorted` function and the `array` variable as a sliceable object to directly modify the original array without creating an additional copy, as stated in the hint provided by the problem statement. Thus, it achieves the desired sorting behavior with a concise and efficient implementation.