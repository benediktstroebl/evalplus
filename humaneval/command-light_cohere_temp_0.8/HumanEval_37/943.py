```python
def sort_even(l: list):
    return sorted(l, key=lambda x: (x, x%2))

#Test the function
[5, 6, 3, 4] = sort_even([5, 6, 3, 4])
[3, 6, 5, 4]

[1, 2, 3] = sort_even([1, 2, 3])
[1, 2, 3]

```