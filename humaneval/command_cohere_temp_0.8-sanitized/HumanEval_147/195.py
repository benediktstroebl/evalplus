def get_max_triples(n):
    # Create the sequence
    a = [i * i - i + 1 for i in range(1, n + 1)]
    
    # Initialize the count of triples
    max_triples = 0
    
    # Consider all possible pairs (i, j) where i < j
    for i in range(n - 1):
        for j in range(i + 1, n):
            # Sum of two values and the remaining value
            remaining = a[j] - a[i - 1]
            
            # Calculate the sets of triplets that have the sum as multiple of 3
            multiple_of_3 = remaining // 3
            triples = (multiple_of_3 * (multiple_of_3 + 1)) // 2
            
            max_triples = max(max_triples, triples)
    return max_triples