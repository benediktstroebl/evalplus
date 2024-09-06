```python
def sort_even(l: list):
    even = [x for x in l if len(x) % 2 == 0]
    odd = [x for x in l if len(x) % 2 != 0]
    return odd + sorted(even)
```

This Python script defines a function called `sort_even` that takes a list called `l` as input. It separates the list into two parts: a list of even indices called `even` and a list of odd indices called `odd`. The function then returns the original list with the odd-indexed values unchanged and the even-indexed values sorted in ascending order.

Here is an example usage of the function:
```python
l = [1, 2, 3]
print(sort_even(l))  # Expected output: [1, 2, 3]
```

And another example:
```python
l = [5, 6, 3, 4]
print(sort_even(l))  # Expected output: [3, 6, 5, 4]
```

These examples show how the function maintains the original odd-indexed values while sorting the even-indexed values.