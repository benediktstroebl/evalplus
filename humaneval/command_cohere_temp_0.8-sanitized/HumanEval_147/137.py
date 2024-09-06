def get_max_triples(n):
    # Create the sequence
    a = [i * i - i + 1 for i in range(1, n + 1)]
    
    # Calculate max triples
    triples = 0
    for i in range(n):
        for j in range(i + 1, n):
            curr = a[i] + a[j]
            valid_triple = False
            for k in range(j + 1, n + 1):
                if curr + a[k] == 0 or curr + a[k] == 3:
                    valid_triple = True
                    break
            if valid_triple:
                triples += 1
    return triples