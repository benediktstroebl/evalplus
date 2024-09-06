```python
def iscube(a):
    # Check if the number is divisible by 2 and then 3
    return not a & 1 and not a & 3
```

The function checks if the number `a` is divisible by 2 and 3 by using bit manipulation. If the number is divisible by both 2 and 3, it returns True, else False. 

This approach gives a linear time solution `O(log a)` where a is the input number.