```python
def unique_digits(xs):
    odd = [x for x in xs if any(int(c) % 2 != 0 for c in str(x))]
    return sorted(odd)
```
```
The function unique_digits(xs) takes a list of integers xs as input and returns a sorted list of elements that contain no even digits. The function first uses a list comprehension to filter out the elements that contain at least one odd digit from the input list xs. Then, it sorts the resulting list in increasing order and returns the sorted result.
```