```python
def triples_sum_to_zero(l: list):
    seen = set()
    for i, x in enumerate(l):
        if not seen:
            continue
        for j, y in enumerate(l[i+1:], i+1):
            if not seen | {x, y}:
                z = l[j+1:]
                if sum(map(lambda p: p[0]+p[1]+p[2], zip(l, z, l[j+1:])) == 0 and x + y + z[0] == 0:
                    return True
            seen.add(y)
    return False
```

The function employs set comprehension and the `enumerate` function to iterate through the list, tracking already seen elements to ensure it examines all possible triple combinations. It then checks whether their sum equals zero and the two remaining sides themselves sum up to zero.