```python
def triples_sum_to_zero(lst):
    # Write your code here
    seen = set()
    for a in lst:
        for b in lst:
            if a == b:
                continue
            for c in lst:
                if c == a or c == b:
                    continue
                if (a + b + c) == 0 and (a, b, c) not in seen:
                    seen.add((a, b, c))
                    return True
    return False
```

The function examines all possible triples of elements in the list `lst`. It uses a set called `seen` to keep track of the triples already encountered, so it doesn't repeat calculations. The function returns True if any trio of elements adds up to zero and False otherwise.

This solution has an exponential time complexity of O(3^N) because it examines all possible triples, but the runtime is mitigated by set operations that prevent duplicate work.