```python
def will_it_fly(q, w):
    return (q == q[::-1] and sum(q) <= w)
```

This function will return True if the list `q` is both palindic (using the slicing technique `q[::-1]` to reverse a list) and its elements' sum is less than or equal to the maximum weight `w`. Otherwise, it will return False. This approach ensures efficiency in determining both conditions.