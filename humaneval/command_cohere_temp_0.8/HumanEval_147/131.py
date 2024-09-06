```python
def get_max_triples(n):
    # Create the sequence
    a = [i * i - i + 1 for i in range(1, n + 1)]
    
    # Initialize the count of triples
    max_triples = 0
    
    # Consider all possible lengths of subsets of size 3
    for subset_size in range(n - 2):
        # Calculate the current count of subsets of size 3
        current_triples = (subset_size * (subset_size + 1) * (subset_size + 2)) // 6
        
        # Calculate the maximum count of triples
        max_triples = max(max_triples, current_triples)
    
    return max_triples
```

The approach exploits the fact that the problem is essentially asking for the maximum number of subsets of size 3 that can form a triangle with an edge sum divisible by 3. The formula `(subset_size * (subset_size + 1) * (subset_size + 2)) // 6` gives the number of ways to choose 3 elements from a set of size `subset_size` such that they form a triangle.

By adjusting the subset size, we can consider all possible triangle configurations and thereby calculate the maximum number of valid triples.