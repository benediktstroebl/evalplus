```python
def will_it_fly(q, w):
    return (q == q[::-1] and sum(q) <= w)
```

This function will return True if the object q will fly, and False otherwise. The object q will fly if it is balanced (it is a palindromic list) and the sum of its elements is less than or equal to the maximum possible weight w. The function uses a logical AND operation to determine if both conditions are met, returning True if so and False if not.