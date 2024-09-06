```python
def triples_sum_to_zero(lst):
    # Write your code here. Read the EMT below.
    seen = set()
    for a in lst:
        for b in lst:
            if a != b and sum(c for c in [a, b] if c in seen) == 0:
                seen.add(a)
                seen.add(b)
                return True
    return False
```

**Explanation**:
1. We use a set `seen` to keep track of already-seen elements to avoid duplicates.
2. We iterate through the list `lst` and consider each element `a` as a potential anchor for a pair that sums to zero.
3. For each element `b` (different from `a`), we calculate the sum of the two elements (`a` and `b`) if they are present in the `seen` set, which is basically a filter to check if they sum up to zero.
4. If the sum is indeed zero, we add both `a` and `b` to the `seen` set and return `True`. If we iterate through all elements without finding such a pair, we return `False`.

The accompanying tests are designed to check if the function correctly identifies valid triplets that sum to zero and also ensure that it correctly handles edge cases. 
```python
test_list = [
    ([1, 3, 5, 0], False),
    ([1, 3, -2, 1], True),
    ([1, 2, 3, 7], False),
    ([2, 4, -5, 3, 9, 7], True),
    ([1], False),
    ([], False),
    ([], True),
    ([0, 0, 0], True),
]

for test in test_list:
    assert triples_sum_to_zero(test[0]) == test[1]
```