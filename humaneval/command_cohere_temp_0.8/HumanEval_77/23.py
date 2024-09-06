```python
def iscube(a):
    # Check if the number is divisible by 2 and then 3
    if a % 2 == 0 and a % 3 == 0:
        return True
    else:
        return False
```

This function `iscube` checks if a number is a cube of some integer by checking if the number is divisible by 2 and then 3. A number is a cube if it is divisible by 2 at least three times and divisible by 3 at least one time. This is equivalent to checking if the number is divisible by 2 and 3 simultaneously.

This approach has a linear time complexity of O(1) since the divisibility checks for 2 and 3 take constant time. Although this is not the most efficient approach, it is straightforward and relatively concise.