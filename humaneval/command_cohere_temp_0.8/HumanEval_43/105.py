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

This function iterates through every element in the list and simply checks if the list has two elements that sum up to zero. It does so by keeping track of all seen elements in a set, if the element is positive, it checks if it has already appeared in the set and if so, it checks if it appears more than once in the list, if it does, the function returns true. This is ensured as if there are two distinct elements, let's say x and y, such that x + y = 0, if x > 0, we insert x into the set, if y is negative, it will be inserted as -y, so (-y) in the set is the same as (x), thus if we encounter y and it is not equal to x, we will insert y into the set, if it is equal to x, we just increment the count of x, which will result in true when checking if the count is more than 1. The inverse is true for the case when x is negative and y is positive.