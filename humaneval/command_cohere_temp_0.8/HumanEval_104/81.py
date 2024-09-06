```python
def unique_digits(x):
    odd = [y for y in x if not any(int(c) % 2 == 0 for c in str(y))]
    return sorted(odd)
```
```
In the function, we iterate over all elements in the list `x`, and for each element `y`, we check if it is divisible by 2, using the condition `any(int(c) % 2 == 0 for c in str(y))`. If it is not divisible by 2, we add it to the list `odd` that we define. Finally, we return the list `odd` sorted in ascending order.
```