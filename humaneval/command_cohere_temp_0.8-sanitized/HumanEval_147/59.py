def get_max_triples(n):
    # Create the sequence
    a = [i * i - i + 1 for i in range(1, n + 1)]
    
    # Initialize variables to track triples and multiples of three
    triples = 0
    multiple_of_three = 0
    
    # Calculate multiples of three and triples
    for i in range(n - 2):
        for j in range(i + 1, n):
            for k in range(j + 1, n + 1):
                if a[i] + a[j] + a[k] % 3 == 0:
                    triples += 1
                if a[i] + a[j] + a[k] % 3 == 0:
                    multiple_of_three += 1
    
    return triples