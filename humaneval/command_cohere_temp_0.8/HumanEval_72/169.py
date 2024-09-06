```python
def will_it_fly(q, w):
    return (q == q[::-1] and sum(q) <= w)
```

This function will return True if the list `q` is both palindic (i.e., identical to its reversed version `q[::-1]`) and the sum of its elements is less than or equal to the given maximum weight `w`. Otherwise, it will return False. This logic follows the problem statement's guidelines to determine if an object will fly based on its balance and weight ratio.