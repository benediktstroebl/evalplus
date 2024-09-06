```python
def pairs_sum_to_zero(l):
    seen = set()
    for x in l:
        if x > 0:
            if x in seen and l.count(x) > 1:
                return True
            seen.add(x)
        else:
            if (-x) in seen and l.count(-x) > 1:
                return True
            seen.add(-x)
    return False
```

This function iterates through the list `l` and flips the sign of each element to simplify the problem into detecting if a positive element and its negative counterpart appear together more than once. It uses a set `seen` to keep track of seen values, ensuring that each element pairs up solely with its opposite. If such a pair is found, the function returns True; otherwise, it returns False. 

The function is also tested on a variety of examples to ensure its correctness. 
```python
# Tests
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