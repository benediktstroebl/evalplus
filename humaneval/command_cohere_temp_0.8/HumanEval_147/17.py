```python
def get_max_triples(n):
    # Create the sequence
    a = [i * i - i + 1 for i in range(1, n+1)]
    
    # Initialize counter for triples
    max_triples = 0
    
    # Calculate valid triples and update max_triples
    for i in range(n-2):
        for j in range(i+1, n-1):
            if (a[i] + a[j] + a[j+1]) % 3 == 0:
                max_triples += 1
    
    return max_triples
```

The script uses nested loops to iterate through all possible triples (i, j, k) of adjacent elements in the sequence `a`, and checks if `a[i] + a[j] + a[k]` is a multiple of 3. The maximum number of valid triples are kept track of in the `max_triples` variable, which is returned once all combinations have been checked.

This approach has a time complexity of O(n^2) due to the nested loops, but this is acceptable given the small size of the input n and the small range of operations within each loop.

The tests will ensure that the function behaves as expected for various values of n, and the `max_triples` value is returned correctly. Feel free to add more tests to cover a broader range of scenarios if necessary!