def get_max_triples(n):
    arr = [i * i - i + 1 for i in range(1, n+1)]
    
    # Calculate maximum number of triples per day for days ranging from 1 to n.
    max_triples = 0
    for i in range(1, n):
        for j in range(i + 1, n):
            if (arr[i] + arr[j] + arr[j-i-1]) % 3 == 0:
                max_triples += 1

    return max_triples