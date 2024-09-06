```python
def will_it_fly(q, w):
    return (sum(q) <= w) and palindrome(q)

def palindrome(q):
    return q == q[::-1]
```

The `will_it_fly()` function uses a boolean OR operation to determine if an object will fly or not. If the sum of the object's elements exceeds the maximum possible weight, it returns `False`, and if the collection is not a palindrome, it also returns `False`. If the sum of the object's elements is less than or equal to the maximum possible weight and the collection is a palindrome, it returns `True`. 

This function ensures that both conditions for an object to fly must be met and returns either `True` or `False` accordingly.