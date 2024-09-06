```python
def triples_sum_to_zero(l: list):
    seen = set()
    for i, x in enumerate(l):
        if not seen:
            continue
        for j, y in enumerate(l[i+1:], i+1):
            if not seen | {x, y}:
                z = sum([x, y, l[j+1]])
                if not z: return True
            seen.add(y)
    return False
```

This code iterates through the list, checking for triples that sum up to zero. It uses a set to keep track of seen elements to ensure that all three elements are distinct. The final line returns False if no such triple is found.  This approach has a time complexity of O(n^2) due to the nested iteration, where n is the length of the input list.