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

This function iterates through the list `l` and uses a set `seen` to keep track of unique integers (positive or negative) that have been encountered so far. For every positive integer `x`, the function checks if `x` is in the set and if there are more than one occurrence of `x` in the list. If both conditions are met, it returns `True`. The function also checks if the negative of `x` meets the conditions, as two negative integers that sum to zero would be considered a valid pair as well. The function returns `False` if no such pair is found after one pass through the list. 

Here is an example usage statement that can be added to the code to test the function:
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

This would test the function against the provided test cases from the problem statement.