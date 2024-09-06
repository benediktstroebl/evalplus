def get_max_triples(n):
    arr = [i * i - i + 1 for i in range(1, n+1)]
    
    # Calculate max triples where a[i] + a[j] + a[k] is a multiple of 3
    # By observing that the necessary conditions are:
    # - The delta of two consecutive terms is either -2 or 2 (to sum up to multiple of 3)
    # - Therefore, for every 3 consecutive terms, there are 2 deltas of 2, and hence 2 triples
    # - Therefore, the number of triples is ceil(n/3) * 2
    return ceil(n/3) * 2