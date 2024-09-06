def get_max_triples(n):
    # Create the sequence
    a = [i * i - i + 1 for i in range(1, n+1)]
    
    # Initialize counter
    max_triples = 0
    
    # Calculate valid triples for each value 'a_i' in the array
    for i in range(n):
        for j in range(i + 1, n):
            k = (i + j) // 2
            if k < j:
                continue
            if a[i] + a[j] + a[k] % 3 == 0:
                max_triples += 1
    
    return max_triples