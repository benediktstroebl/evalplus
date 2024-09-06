def get_max_triples(n):
    # Create the sequence
    a = [i * i - i + 1 for i in range(1, n+1)]
    
    # Initialize variables to track unique triples and multiples of 3
    triples = 0
    multiple_of_3 = 0
    
    # Loop through all combinations of size 3
    for i in range(n-2):
        for j in range(i+1, n):
            current_sum = a[i] + a[j] + a[j+1]
            if current_sum % 3 == 0:
                triples += 1
                multiple_of_3 += 1
    
    return triples // 3