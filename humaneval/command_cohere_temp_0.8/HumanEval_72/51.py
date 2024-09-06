```python
def will_it_fly(q, w):
    return (q == q[::-1] and sum(q) <= w)
```

This function will return True if the list `q` is both balanced (i.e., a palindrome) and its sum is less than or equal to the maximum weight `w`. Otherwise, it will return False. Such behavior is captured by the provided examples in the problem statement.