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

This function iterates through the list, tracking positive and negative occurrences of numbers in the 'seen' set. If both the positive and negative occurrences of a number are encountered more than once, the function returns 'True'. Otherwise, it returns 'False'. This is done for all numbers in the list. 
This approach takes advantage of the fact that sets don't allow duplicates, so we can use them to efficiently track occurrences of numbers without having to worry about multiple representations of the same number.