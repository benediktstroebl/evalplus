```python
def will_it_fly(q, w):
    return (str(q) == str(q)[::-1]) and sum(q) <= w
```

The function `will_it_fly` uses a concise one-liner to determine whether the list `q` is palindic (`str(q) == str(q)[::-1]`). It returns True if the sum of the elements of the list does not exceed the maximum weight `w`. As a result, it determines whether or not the object will fly.

This approach takes into account both the balance condition and the weight condition, returning True if the object will fly and False otherwise.

To ensure proper functionality, it is important to input the values as either a list or a single integer, as the function assumes either a list or a single integer for the input.