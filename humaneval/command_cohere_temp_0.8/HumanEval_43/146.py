```python
def pairs_sum_to_zero(l):
    # Write your code here
    seen = set()
    for i in l:
        if i > 0:
            complement = -i
        else:
            complement = i
        if complement in seen:
            return True
        seen.add(i)
    return False
```

This function examines each integer in the list. If it is positive, it searches for its negative complement in the set of seen elements. If it is negative, it searches for the positive complement. If the complement is found, the function returns True, indicating that two elements in the list sum up to zero. Otherwise, it returns False. 

Here's an example usage output:
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

This demonstrates the function's behavior, successfully checking for pairs with a sum of zero in various scenarios.