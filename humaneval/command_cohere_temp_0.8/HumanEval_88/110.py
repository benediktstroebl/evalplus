```python
def sort_array(array):
    odd, even = array[:1], array[-1:]
    if sum(map(len, (odd, even))) % 2 == 0:
        array = sorted(array)[::-1]
    return array
```

This Python script solves the problem by dividing the array into two parts: a first-element subset (`odd`) and a last-element subset (`even`). If the total length of these two subsets is even, it sorts the entire array in reverse order; otherwise, it leaves the array as is. This logic takes advantage of the sorting order while fulfilling the directive to reverse the order only when necessary.