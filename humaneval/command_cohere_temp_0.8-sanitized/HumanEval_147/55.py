def get_max_triples(n):
    arr = [i * i - i + 1 for i in range(1, n+1)]
    
    # Calculate max triples where a[i] + a[j] + a[k] is a multiple of 3
    # by considering all possible pairs and triples and optimizing with exclusion sets.
    counter = 0
    exclude_sets = []
    
    for i in range(n):
        for j in range(i + 1, n):
            exclude_set = set([arr[i - 1], arr[j - 1]])
            for k in range(j + 1, n):
                if arr[k - 1] not in exclude_set:
                    counter += 1
                    exclude_sets.append(exclude_set | {arr[k - 1]})
    
    return counter