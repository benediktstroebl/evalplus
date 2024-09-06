def get_max_triples(n):
    # Create the sequence
    a = [i * i - i + 1 for i in range(1, n+1)]
    
    # Initialize variables to track occurrences of a[i] and a[i] + a[j] values
    # that are multiples of 3 (and therefore their combinations will also be multiples of 3)
    # Also track occurrences of triples (a[i], a[j], a[k]) where i < j < k
    triples = 0
    values = [0] * (n * 2 + 1)
    for i in range(n):
        for j in range(i + 1, n + 1):
            required = a[i] + a[j]
            if required % 3 == 0:
                # Mark the occurrence of this value as positive
                values[required] += 1
            else:
                # If the value is 2 mod 3, it will be a 'negative' occurrence
                # as it needs to be combined with another value to yield a multiple of 3
                values[required] -= 1
            
            # Now check for the triple
            if i < j:
                # For triples (a[i], a[j], a[k]), we only consider cases where i < j < k
                # so we can ignore the case where i == j
                triples += values[a[i] + a[j]]
                values[a[i] + a[j]] -= 1
    
    return triples