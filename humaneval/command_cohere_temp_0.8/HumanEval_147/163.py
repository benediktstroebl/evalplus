```python
def get_max_triples(n):
    # Create the sequence
    a = [i * i - i + 1 for i in range(1, n+1)]
    
    # Calculate the maximum triples
    triples = 0
    for i in range(n):
        for j in range(i + 1, n):
            curr = a[i] + a[j]
            if curr % 3 == 0:
                triples += 1
    return triples
```

The Python script creates the array `a` as specified in the problem statement. It then calculates the sum of values `a[i] + a[j]` for all pairs of indices `i` and `j` where `i < j` which would respect the condition that the sum is a multiple of 3. It uses two nested loops to iterate over all possible pairs of indices and checks if the condition is met for each pair to increment the `triples` count. The function ultimately returns the total count of eligible triples. 

This solution would result in a maximum of one triple per value of `n` as it is the most efficient way to achieve the problem goal.