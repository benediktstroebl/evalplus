```python
def get_max_triples(n):
    # Create the sequence
    a = [i * i - i + 1 for i in range(1, n + 1)]
    
    # Initialize counter for triples
    max_triples = 0
    
    # Consider all possible pairs (a[i], a[j])
    for i in range(n - 1):
        for j in range(i + 1, n):
            # Calculate the potential third element a[k]
            k = (a[i] + a[j] + 1) // 3
            # Adjust the index to handle both positive and negative offsets
            k = min(k, j - i)
            k = max(k, j - i - 1)
            if k != n:
                max_triples += 1
    
    return max_triples
```

The approach is to iterate through all possible pairs of elements (`a[i]` and `a[j]`) in the sequence, and then determine the potential third element `a[k]` such that the condition is satisfied. The variable `max_triples` is incremented each time a valid triple is found.