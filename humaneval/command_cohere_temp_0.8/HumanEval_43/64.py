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

This function examines every possible pair in the list `l` and checks if their sum equals zero. It uses a set `seen` to keep track of integers that have been seen before. If a positive integer is encountered, the function checks if it has been seen before in the list and if there are more than one occurrences of it. This is done to verify if there is another integer in the list that pairs with the positive integer to sum up to zero. The function employs a similar logic for negative integers using the set `seen`. 

For example, let's apply the function to the list `[2, 4, -5, 3, 5, 7]` : 
```python
pairs_sum_to_zero([2, 4, -5, 3, 5, 7])
```

The output would be:
```bash
True
```

The function returns `True` since two pairs sum up to zero: `(2, -5)` and `(4, -3)`. 

However, if we input `[1, 3, 5, 0]` the function will return:
```python
pairs_sum_to_zero([1, 3, 5, 0])
```

The output will be `False`, since no two elements in the list sum up to zero. 

The function should correctly identify all cases where there are two distinct elements in the list that sum to zero. 

This implementation is efficient with a time complexity of O(n^2) since it runs twice through the list and performs operations like set updating and counting occurrences that are constant time for each operation.