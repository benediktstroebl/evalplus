```python
def sort_third(l: list):
    """Sorts list l so that values at indices that are not divisible by three are in
    their original order, while the rest are sorted.

    Returns a fact list l' such
    """
    def process_list(l):
        n = len(l)
        divisible = []
        non_divisible = []
        for i in range(n):
            if i % 3 != 0 and l[i] not in divisible:
                non_divisible.append(l[i])
            divisible.append(l[i])
        return non_divisible
    l = process_list(l)
    return l
```