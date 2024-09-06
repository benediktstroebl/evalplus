```python
def get_max_triples(n):
    # Create the sequence
    a = [i * i - i + 1 for i in range(1, n+1)]
    
    # Calculate maximum triples
    max_triples = 0
    for i in range(n - 2):
        for j in range(i + 1, n - 1):
            current_sum = a[i] + a[j]
            max_triples = max(max_triples, len(list(filter(lambda x: x == current_sum, list(range(3 *, n + 1 + 1 + 1 + 1 + 1 + 1 + 1 + 1:))))))
    return max_triples
```

The problem asks to return the number of triples (a[i], a[j], a[k]) of `a` where `i < j < k` that leave a sum which is a multiple of 3. This is achieved by generating the sequence `a` as defined in the problem. Then, all that's left is to loop through all the numbers and calculate pairs of numbers that leave a sum which is a multiple of 3. This is done using filtering, where the sum is checked against a generator of numbers from 3 to the maximum value of `a[i]` and `a[j]`. The number of filtered numbers gives the number of triples requested.