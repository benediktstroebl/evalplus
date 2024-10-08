def get_max_triples(n):
    # Create the sequence
    a = [i * i - i + 1 for i in range(1, n+1)]
    
    # Initialize the count of triples
    max_triples = 0
    
    # Consider all possible pairs of elements in the sequence
    for i in range(n-1):
        for j in range(i+1, n):
            # Calculate the potential 3rd element
            k = (a[i] + a[j] + a[k]) / 3
            # Adjust the loop to find the 3rd element
            for k_check in range(min(i, j), k):
                if a[k_check] == k:
                    max_triples += 1
    
    return max_triples