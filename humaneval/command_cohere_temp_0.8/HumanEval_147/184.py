```python
def get_max_triples(n):
    # Create the sequence
    a = [i * i - i + 1 for i in range(1, n + 1)]
    
    # Calculate the maximum triples
    triples = 0
    for i in range(n):
        for j in range(i + 1, n):
            curr = a[i] + a[j]
            if curr % 3 == 0:
                # Valid triplet
                triples += 1
    return triples
```

The solution leverages Python's list comprehension and nested loops to generate the array `a` based on the problem's provided formula. It then counts valid triples of `a` where the sum is a multiple of 3, achieving this by directly iterating through all possible pairs of indices and checking if their corresponding values sum up to a multiple of 3.

This direct approach, without any complex optimizations, results in a clear and concise solution that is easy to understand and efficiently solves the problem. The function's performance is suitable for reasonably sized inputs in a competitive coding context.