```python
def triples_sum_to_zero(lst):
    # Write your code here. Read the markdown for more info on the problem.
    seen = set()
    for a in lst:
        for b in lst:
            if a != b and sum(c for c in [a, b] if c in seen and c != 0) == 0:
                return True
            seen.add(a)
    return False
```

This code uses a set and iterates over each element in the list. It also checks for both positive and negative versions of each element to find all potential triple combinations.