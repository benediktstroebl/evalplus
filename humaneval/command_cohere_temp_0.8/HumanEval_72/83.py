```python
def will_it_fly(q, w):
    return (len(q) > 1 and sum(q) <= w and q == q[::-1])
```

The function `will_it_fly` uses three conditional checks to determine if the given object `q` will be able to fly:
1. The length of the object `q` is greater than `1` to ensure it is a list or tuple.
2. The `sum` of the elements in `q` is less than or equal to the maximum weight `w`.
3. The object `q` is symmetric (or palindromic), meaning it is equal to its reversed version `q[::-1]`.

The function will return `True` if all conditions pass, and `False` otherwise, correctly solving the problem. 

This approach gives a concise solution by explicitly employing the conditions laid out in the problem statement.