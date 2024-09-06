def get_max_triples(n):
    arr = [i * i - i + 1 for i in range(1, n+1)]
    
    # Calculate occurrences 3 in arr[i] + arr[j] + arr[k]
    occurrences = [[0] * 3 for _ in range(n)]
    for i in range(n):
        for j in range(i + 1, n):
            for k in range(j + 1, n):
                occurrences[i][0] += occurrences[j][1] + occurrences[k][2] == 3
                occurrences[i][1] += occurrences[j][2] + occurrences[k][0] == 3
                occurrences[i][2] += occurrences[j][0] + occurrences[k][1] == 3
    
    # Calculate the maximum number of triples
    max_triples = sum([min(x) for x in occurrences])
    
    return max_triples