def get_max_triples(n):
    # Create the sequence
    a = [i * i - i + 1 for i in range(1, n + 1)]
    
    # Calculate the maximum triples
    # Consider all possible pairs as (a[i], a[j])
    max_pairs = len(a) - 1
    # Count the valid triples where the sum is multiple of 3
    sum_triple_3 = 0
    for i in range(len(a)):
        for j in range(i + 1, len(a)):
            sum_triple_3 += sum(a[i:j+1]) // 3
    
    return max_pairs - sum_triple_3