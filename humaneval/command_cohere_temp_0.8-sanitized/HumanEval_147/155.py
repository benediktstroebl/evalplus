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