```python
def get_max_triples(n):
    # Create the sequence
    a = [i * i - i + 1 for i in range(1, n+1)]
    
    # Initialize counter
    max_triples = 0
    
    # Calculate valid triples for each value 'a_i' in the array
    for i in range(n):
        for j in range(i + 1, n):
            k = (i + j) // 2
            if k < j:
                continue
            if a[i] + a[j] + a[k] % 3 == 0:
                max_triples += 1
    
    return max_triples
```

The approach is to iterate through the array and find all valid triples (a[i], a[j], a[k]) where `i < j < k` and `a[i] + a[j] + a[k]` is a multiple of 3. The center index `k` is found by averaging `i` and `j`, and then checking if `k` is still less than `j` to ensure the triple is in a valid order. The code is self-contained and should run correctly given the prompt.