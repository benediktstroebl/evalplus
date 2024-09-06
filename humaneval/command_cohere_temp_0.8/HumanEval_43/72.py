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

This function iterates through the list `l` and uses a set `seen` to keep track of elements encountered while looping. When a positive integer is encountered, the function checks if it is already in the set and if there are more than one occurrence of it in the list. If both conditions are met, it returns `True`. This is also done for negative versions of the numbers to check if two negatives sum up to zero. The overall time complexity of this approach is O(n log n) where n is the length of the input list `l`, due to the nested iteration and set operations.