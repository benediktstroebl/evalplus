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

The solution is based on directly generating the array `a` as specified in the problem statement. Then, we iterate through the array and find all valid triples that satisfy the condition `a[i] + a[j] + a[k] == 0 (mod 3)` where `i < j < k`.

To optimize the calculation, we avoid duplicates by utilizing the fact that switching the order of `j` and `j-i-1` doesn't change the result. So, we iterate through `j` values between `i+1` and `n` and calculate the corresponding `i` values with the constraint `j > i`.