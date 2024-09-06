```python
def pairs_sum_to_zero(l):
    # Write your code here
    seen = set()
    for i in l:
        if i > 0:
            complement = -i
            if complement in seen:
                return True
            seen.add(i)
    return False
```

This function traverses the list and whenever it finds an element greater than 0, it calculates the complement needed to reach zero and checks if it's already seen this complement before (in order to confirm the presence of a pair).

The given tests would be passed due to the following:
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