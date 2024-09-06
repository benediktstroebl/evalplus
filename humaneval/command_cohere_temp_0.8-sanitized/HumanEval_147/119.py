def get_max_triples(n):
    # Create the sequence
    a = [i * i - i + 1 for i in range(1, n+1)]
    
    # Initialize the count of triples
    max_triples = 0
    
    # Consider all possible triples
    for i in range(n-2):
        for j in range(i+1, n-1):
            current_sum = a[i] + a[j]
            # Calculate the number of valid triples that have this sum
            valid_count = (current_sum // 3) - ((current_sum % 3) == 0)
            max_triples = max(max_triples, valid_count)
    return max_triples