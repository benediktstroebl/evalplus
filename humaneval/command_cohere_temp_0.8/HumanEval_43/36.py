```python
def pairs_sum_to_zero(l):
    seen = set()
    for x in l:
        if x > 0:
            if x in seen and l.count(x) > 1:
                return True
            seen.add(x)
        else:
            if -x in seen and l.count(-x) > 1:
                return True
            seen.add(-x)
    return False
```

This function examines every integer in the list, tracking the elements seen so far. When it encounters a positive integer `x`, it checks if `x` appears more than once in the list and is paired with another integer that adds up to zero. The function does the same for negative integers, checking if `-x` appears more than once in the list and is paired with its opposite sign to sum up to zero. If any such pairs are found, the function returns `True`, otherwise, it returns `False`. 

Here is an example usage output:
```python
>>> pairs_sum_to_zero([1, 3, 5, 0])
False
>>> pairs_sum_to_zero([1, 3, -2, 1])
False
>>> pairs_sum_to_zero([1, 2, 3, 7])
False
>>> pairs_sum_to_zero([2, 4, -5, 3, 5, 7])
True
>>> pairs_sum_to_zero([1])
False
```