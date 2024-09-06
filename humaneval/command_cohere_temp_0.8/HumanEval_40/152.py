```python
def triples_sum_to_zero(lst):
    # Write your code here
    seen = set()
    for a in lst:
        for b in lst:
            if a != b and sum([a, b, c]) == 0 and (a, b, c) not in seen:
                seen.add((a, b, c))
                if len(seen) == 3:
                    return True
    return False
```

The function `triples_sum_to_zero` works by checking every possible pair out of the elements in the list, and checking whether the third element that gives a sum of zero exists and is not already paired with another element in the list. The function returns True if a trio is found and False otherwise.