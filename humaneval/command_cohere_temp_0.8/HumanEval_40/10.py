```python
def triples_sum_to_zero(l: list):
    """
    Returns True if three distinct elements in the list sum up to zero, False - otherwise.
    """
    seen = set()
    for i, x in enumerate(l):
        if x < 0:
            for j, y in enumerate(l[i+1:]):
                if y < 0 and x + y > 0 and j != i + 1 and (i, x, y) not in seen:
                    seen.add((i, x, y))
                    if l[k] > 0 and x + y + l[k] == 0 and k != i and k != j:
                        return True
                        break
    return False
```
The code examines each pair of elements in the list that are followed by another element, specifically checking if their sum is less than zero. If so, it determines if the third distinct element will make their sum zero. It returns True if a such triplet is found, and False - otherwise. The algorithm runs in O(n^2) due to the nested loop and O(n) for the eventual linear pass through the list.