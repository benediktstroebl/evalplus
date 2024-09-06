```python
def get_max_triples(n):
    # Create the sequence
    a = [i * i - i + 1 for i in range(1, n+1)]
    
    # Calculate maximum triples
    max_triples = 0
    for i in range(n - 2):
        for j in range(i + 1, n - 1):
            sum_ = a[i] + a[j] + a[j + 1]
            if sum_ % 3 == 0:
                max_triples += 1
    return max_triples
```
This script creates the sequence a[i] for i in range(1, n+1) as defined in the problem. It then iterates through all possible pairs of values i and j, and checks if the sum of a[i], a[j], and a[j + 1] is a multiple of 3. If it is, it increments the max_triples variable. Finally, it returns the max_triples variable.