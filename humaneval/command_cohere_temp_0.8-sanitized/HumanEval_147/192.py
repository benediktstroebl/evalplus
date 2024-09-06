def get_max_triples(n):
    arr = [i * i - i + 1 for i in range(1, n+1)]
    
    # Calculate occurrences 3 in arr[i] + arr[j] + arr[k]
    occurrences = []
    for i in range(n):
        for j in range(i + 1, n):
            for k in range(j + 1, n):
                if (arr[i] + arr[j] + arr[k]) % 3 == 0:
                    occurrences.append(1)
                else:
                    occurrences.append(0)
    
    # Now occurrences has max number of triples for each i, j, k
    return max(occurrences)