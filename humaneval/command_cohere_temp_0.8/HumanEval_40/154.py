```python
def triples_sum_to_zero(l: list):
    seen = set()
    for a in l:
        if a == 0:
            continue
        for b in l:
            if a + b in seen:
                continue
            for c in l:
                if a + b + c == 0 and a != c and b != c:
                    return True
            seen.add(a + b)
    return False
```

This function takes a list of integers l as input and checks if there are three distinct elements in the list whose sum is zero. It implements a nested loop structure where it loops through all possible pairs of elements (a, b) and checks if the addition of a third element c results in a sum of zero. The function returns True if such a triplet is found and False otherwise.