```python
def get_max_triples(n):
    # Create the sequence
    a = [i * i - i + 1 for i in range(1, n+1)]
    
    # Calculate the maximum triples
    triples = 0
    for i in range(n):
        for j in range(i + 1, n):
            if (a[i] + a[j] + a[j-i-1]) % 3 == 0:
                triples += 1
    return triples
```

The problem can be solved by generating the array `a` as required in the prompt. Then, we iterate through the array elements and find all the valid triples `(a[i], a[j], a[k])` where `i < j < k` that satisfy the condition `a[i] + a[j] + a[k] == 0 (mod 3)`. We count the valid triples and return the count.

The code is structured into a single, self-contained function `get_max_triples` that takes an integer `n` as input and returns the number of triples as described in the problem. This approach follows the principles of Clean Code, which emphasizes writing concise, logical, and readable code.