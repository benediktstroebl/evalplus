```python
def will_it_fly(q, w):
    return (len(q) > 1 and q == q[::-1] and sum(q) <= w)
```

The function `will_it_fly` uses a recursive approach to check if the list is palindrome by comparing the list to its reverse (`q == q[::-1]`). If the list has more than one element and is a palindrome, it moves to the next condition to verify if the sum of the list's elements is less than or equal to the maximum weight (`sum(q) <= w`). If all conditions are met, it returns `True`; otherwise, it returns `False`. 

This approach ensures that the function considers both balance and weight constraints when determining if an object will fly.