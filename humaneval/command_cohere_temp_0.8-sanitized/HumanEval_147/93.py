def get_max_triples(n):
    # Create the sequence
    a = [i * i - i + 1 for i in range(1, n + 1)]
    
    # Calculate the maximum triples
    # Consider all possible combinations of size 3 from the sequence
    # Count the valid ones (where the sum is divisible by 3)
    max_triples = 0
    for i in range(n - 2):
        for j in range(i + 1, n - 1):
            valid = True
            sum_ = a[i] + a[j] + a[n - 1]
            if sum_ % 3:
                valid = False
            if valid:
                max_triples += 1
    return max_triples