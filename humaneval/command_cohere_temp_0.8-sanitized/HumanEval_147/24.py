def get_max_triples(n):
    arr = [i * i - i + 1 for i in range(1, n+1)]
    
    # Calculate occurrences 3 in arr[i] + arr[j] + arr[k]
    occurrences = [[0 for i in range(n)] for j in range(3)]
    
    for i in range(n):
        for j in range(i + 1, n):
            for k in range(j + 1, n):
                if arr[i] + arr[j] + arr[k] >= 3:
                    occurrences[arr[i] + arr[j] + arr[k]][i] += 1
                    occurrences[arr[i] + arr[j] + arr[k]][j] += 1
                    occurrences[arr[i] + arr[j] + arr[k]][k] += 1
    
    max_triples = 0
    for i in range(3):
        for j in range(3):
            if i != j:
                max_triples += occurrences[i][j] // 2
    
    return max_triples