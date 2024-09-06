```python
def get_max_triples(n):
    # Create the sequence
    a = [i * i - i + 1 for i in range(1, n + 1)]
    
    # Initialize the count of triples
    max_triples = 0
    
    # Consider all possible pairs (a[i], a[j])
    for i in range(n - 1):
        for j in range(i + 1, n):
            # Calculate the potential triples (a[i], a[j], a[k]) with i < j < k
            k = j + 1
            while k < n:
                potential_triple = a[i] + a[j] + a[k]
                if potential_triple % 3 == 0:
                    max_triples += 1
                k += 1
    
    return max_triples
```

The approach is to generate the array `a` as specified in the problem. We then iterate over all possible pairs of indices (`i` and `j`) and for each pair, we iterate over all possible subsequent indices `k` to check if the corresponding triple (`a[i]`, `a[j]`, `a[k]`) satisfies the condition that their sum is divisible by 3. The max_triples count is incremented each time such a qualifying triple is found.