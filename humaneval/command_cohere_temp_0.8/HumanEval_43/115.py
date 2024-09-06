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

This function iterates through every element in the list and simply checks whether the list has two (multiplied) elements that sum up to zero. It does so by keeping a track of all seen elements in a set, if an element x is encountered and it is positive, then we want to track the negated value -x and vice versa. Then we check if this element (or its negation) has been previously seen, if it has, then we check if it appears more than once in the list, if it does, then we have our two elements that sum to zero! Otherwise, we move on and check the next element.