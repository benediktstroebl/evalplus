```python
def get_max_triples(n):
    arr = [i * i - i + 1 for i in range(1, n+1)]
    
    # Calculate max triples where a[i] + a[j] + a[k] is a multiple of 3
    # By condition, either a[i] or a[j] or a[k] has to be 3 modulo 3
    # So, the only permutation possible is (3mod3, 1mod3, 0mod3) OR (0mod3, 1mod3, 3mod3)
    # Also, you need not consider all 3 elements from the set {a[0], a[1], ... a[n-1]}
    # Any two arbitrary elements can be selected, and the third element can be determined
    # based on the condition mentioned above.
    max_triples = (arr.count(1) // 3) * 2
    
    return max_triples
```

The function `get_max_triples()` creates the array `arr` consisting of the given values `i * i - i + 1` for `i = 1, 2, ..., n`. It then calculates the number of triples that satisfy the condition `a[i] + a[j] + a[k] == 0 (mod 3)` and returns the result. Two iterations are required to count the numbers that are 1 modulo 3. The final result is returned as the maximum number of triples satisfying the condition.