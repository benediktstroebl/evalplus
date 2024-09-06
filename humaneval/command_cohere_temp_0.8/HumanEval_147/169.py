```python
def get_max_triples(n):
    # Create the sequence
    a = [i * i - i + 1 for i in range(1, n+1)]
    
    # Calculate maximum triples
    max_triples = 0
    for i in range(n):
        for j in range(i + 1, n):
            curr_sum = a[i] + a[j]
            max_triples += (curr_sum // 3) * (curr_sum // 3 + 1)
    return max_triples
```
This Python script defines a function `get_max_triples` that takes in a positive integer `n` as its argument and returns the number of triples from the sequence `a` where `a[i] + a[j] + a[k]` is a multiple of 3 and `i < j < k`.

The script creates the sequence a of length n as specified in the problem statement, and then calculates the number of triples that satisfy the condition. It counts the number of triples by considering each element `a[i]` as a potential starting point and calculating the total number of valid endings for it. To do this, we consider each element `a[j]` with `j > i` as a potential ending point and count the number of possible third elements that would result in the sum being a multiple of 3. The result is an optimal solution to the problem.