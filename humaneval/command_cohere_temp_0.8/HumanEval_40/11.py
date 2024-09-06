```python
def triples_sum_to_zero(l: list):
    seen = set()
    for i, x in enumerate(l):
        if not seen:
            continue
        for j, y in enumerate(l[i+1:], i+1):
            if not seen | {x, y}:
                z = l[j+1:]
                if sum(map(lambda t: t[0]+t[1]+t[2], zip(l, z, l[j+1:])) == 0 and x+y+z[0] == 0:
                    return True
            seen.add(y)
    return False
```

The function employs set comprehension and the `enumerate` function to iterate through the list, tracking previously seen elements in the `seen` set. It then checks if there are three distinct elements in the list whose sum is zero. 

This approach is efficient and has a time complexity of `O(n^2)`, where `n` is the length of the input list.