def get_max_triples(n):
    arr = [i * i - i + 1 for i in range(1, n+1)]
    
    # Calculate the maximum number of triples where a[i] + a[j] + a[k] is a multiple of 3.
    # We count for each a[i] the number of corresponding valid pairs (j, k)
    cache = [0] * (n + 1)
    for j in range(1, n):
        for k in range(j + 1, n):
            if (arr[j] + arr[k]) % 3 == 0:
                cache[j] += 1
    
    # The answer is the sum of valid pairs for a[1..n]
    return sum(cache) - cache[0]