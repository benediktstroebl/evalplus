def get_max_triples(n):
    arr = [i * i - i + 1 for i in range(1, n+1)]
    # Calculate the maximum number of triples using a counter
    counter = 0
    for i in range(n - 2):
        for j in range(i + 1, n):
            if arr[i] + arr[j] == arr[j] + arr[j + 1]:
                counter += 1
    return counter