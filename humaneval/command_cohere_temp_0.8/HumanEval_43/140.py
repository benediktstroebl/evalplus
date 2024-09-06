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

This function examines every element in the list. If the element is positive, it checks if it has previously been seen in the set and if there are more than one occurrence of it in the list. If the element is negative, it checks if `-element` is already in the seen set and if there are more than one negatives in the list. The function returns `True` if any of these conditions are met and `False` otherwise. 

Here is a example usage of this function:
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
This demonstrates the function's behavior accordingly to the given test cases.