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

This function iterates through every element in the list and simply checks if the element is in the set `seen`. It initially establishes a set `seen` to effectively keep track of elements encountered, regardless of their sign. If the element is positive, it checks if it has previously appeared in the list and if its count is greater than one. Conversely, if the element is negative, it checks if its negation has previously appeared and if that count is also greater than one. Ultimately, if any of these conditions are met, the function returns `True`, signifying the existence of two elements that sum up to zero. 

This approach ensures efficiency and simplicity, enabling the function to seamlessly handle the problem presented.