```python
def triples_sum_to_zero(lst):
    # Using recursion to fix two elements and check the third one
    return any(lambda x, y, z: x + y + z == 0 for x in lst for y in lst if x != y for z in lst if x != z and y != z)
```

The script uses a recursive function, which creates a generator of triples, excluding duplicates, and checks if their sum is equal to zero. The `any()` function is then used to check if any of the triples have a sum of zero.