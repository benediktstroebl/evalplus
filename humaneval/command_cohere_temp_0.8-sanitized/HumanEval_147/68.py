def get_max_triples(n):
    # Create the sequence
    a = [i * i - i + 1 for i in range(1, n + 1)]
    
    # Initialize the count of triples
    max_triples = 0
    
    # Consider all possible pairs (a[i], a[j])
    for i in range(n - 1):
        for j in range(i + 1, n):
            # Calculate the potential triples (a[i], a[j], a[k]) with i < j < k
            k = j + 1
            while k < n:
                potential_triple = a[i] + a[j] + a[k]
                if potential_triple % 3 == 0:
                    max_triples += 1
                k += 1
    
    return max_triples