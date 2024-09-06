```python
def will_it_fly(q, w):
    return (q == q[::-1] and sum(q) <= w)
```

This function will return True if the list `q` is both balanced (i.e., it is a palindrome) and the sum of its elements is less than or equal to the given maximum weight `w`. Otherwise, it will return False. 

For example:
```python
will_it_fly([1, 2], 5) # Output: False 
# 1 + 2 is less than the maximum possible weight, but it's unbalanced.

will_it_fly([3, 2, 3], 1) # Output: False
# it's balanced, but 3+2+3 is more than the maximum possible weight.

will_it_fly([3, 2, 3], 9) # Output: True
# 3+2+3 is less than the maximum possible weight, and it's balanced.

will_it_fly([3], 5) # Output: True
# 3 is less than the maximum possible weight, and it's balanced.
```