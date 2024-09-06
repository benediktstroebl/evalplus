def get_max_triples(n):
    arr = [i * i - i + 1 for i in range(1, n+1)]
    
    # Calculate max triples where a[i] + a[j] + a[k] is a multiple of 3
    # By condition, either a[i] + a[j] is a multiple of 3, or a[j] + a[k] is a multiple of 3
    # or a[i] + a[k] is a multiple of 3
    num_triple_1 = arr[0] // 3
    num_triple_2 = (arr[0] + 1) // 3
    num_triple_3 = (arr[0] + 2) // 3
    max_triples = num_triple_1 + num_triple_2 + num_triple_3
    
    for i in range(1, n):
        # For each element, check if arr[i] + arr[i-1] is a multiple of 3
        cur_triple = (arr[i] + arr[i-1]) // 3
        max_triples = max(max_triples, cur_triple)
    
    return max_triples