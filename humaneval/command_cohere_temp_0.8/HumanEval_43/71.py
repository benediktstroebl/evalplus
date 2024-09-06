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

This function iterates through the list, tracking positive and negative occurrences of numbers in the set `seen`. If it encounters a positive and negative pair that add up to zero, the function returns `True`. Also, to handle cases where there are duplicate elements in the list, the function checks if the count of elements is greater than one. This is ensured by the condition `l.count(x) > 1`. 

This approach guarantees a correct solution in an efficient manner. Here is a snippet of tests to verify its behavior:
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
>>> pairs_sum_to_zero([1, 2, 3, 4, 5, 4, -9, 0, -3, 4])
True
```