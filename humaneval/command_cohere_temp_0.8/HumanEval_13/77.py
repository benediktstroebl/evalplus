```python
def greatest_common_divisor(a, b):
    """ Returns the greatest common divisor of two integers a and b """
    if a == 0:
        return b
    return greatest_common_divisor(b%a, a)
```

This recursive approach to finding the greatest common divisor is very efficient and elegant, but it's good to be mindful of potential issues with recursion depth in some contexts. If there are concerns about performance or memory limitations, a iterative approach may be preferable. However, the elegance and readability of this recursive solution make it a favorite among Pythonists.