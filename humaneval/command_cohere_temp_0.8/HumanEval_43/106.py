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

This function iterates through the list, tracking elements in a set (to avoid repeating operations on the same element). For positive elements, it checks if the element has appeared more than once and if its negated value is also in the set. Similarly, for negative elements, it checks if the element has appeared more than once and if its positive counterpart is in the set. If either of these conditions is true, it returns True; otherwise, it returns False. 

The function is optimized to use the set data structure for checking duplicate values and factoring out the negation of the element. This makes the function efficient with a time complexity of O(n), where n is the length of the input list.