```python
def get_max_triples(n):
    # Create the sequence
    a = [i * i - i + 1 for i in range(1, n + 1)]
    
    # Initialize the count of triples
    max_triples = 0
    
    # Consider all possible lengths of triples
    for length in range(3, n + 1):
        # Calculate the number of valid triples of the given length
        triple_count = (n - length + 1) * (length - 2) / 2
        
        # Update the maximum number of triples
        max_triples = max(max_triples, triple_count)
    
    return max_triples
```

The function creates the array a as described in the prompt and then calculates the number of valid triples for each possible length of three or more elements from the array. The maximum number of triples across all lengths is then returned. The solution optimally calculates the answer without extra space overhead.