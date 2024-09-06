```python
def sort_array(array):
    odd, even = array[:1], array[-1:]
    if sum(map(len, (odd, even))) % 2 == 0:
        array = sorted(array)[::-1]
    return array
```

This Python script solves the problem by splitting the array into two parts: a first-element subset and a last-element subset. Then, it checks whether the sum of their lengths modulo 2 is equal to 0 to determine whether to reverse the entire array for the sorting process. Ultimately, it returns the properly sorted array based on the sum of the lengths of the first and last elements of the array.