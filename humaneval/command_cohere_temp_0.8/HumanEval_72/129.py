```python
def will_it_fly(q, w):
    return (q == q[::-1] and sum(q) <= w)
```

This function will return True if the object q will be able to fly, and False otherwise. The function checks if the list (or string) q is palindromic and if the sum of its elements is less than or equal to the maximum possible weight w. The requirement that the sum of the elements of the list must be less than or equal to the maximum possible weight is meant to assure that the palindrome, if too large, would not be too heavy to fly.