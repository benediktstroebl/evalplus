def get_max_triples(n):
    arr = [i * i - i + 1 for i in range(1, n+1)]
    
    # Calculate sum of adjacent pairs to check triples
    pairs_sum = [arr[i] + arr[i-1] for i in range(1, n)]
    
    # Count multiples of 3
    triple_count = sum(1 for x in pairs_sum if x % 3 == 0)
    
    return triple_count