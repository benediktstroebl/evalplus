```python
def pairs_sum_to_zero(l):
    # Write your code here
    seen = set()
    for i in l:
        if i > 0:
            if i in seen and l.count(i) > 1:
                return True
            seen.add(i)
        else:
            if -i in seen and l.count(-i) > 1:
                return True
            seen.add(-i)
    return False
```

This function examines each integer in the list and adds it to a set. If it encounters a second occurrence of that element, whether it is positive or negative, it returns True. Otherwise, it returns False. This algorithm is relatively efficient, with a time complexity of O(n), where n is the length of the input list.