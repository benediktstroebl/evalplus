def get_max_triples(n):
    arr = [i * i - i + 1 for i in range(1, n+1)]
    
    # Calculate max triples where a[i] + a[j] + a[k] is a multiple of 3
    # By observing that the necessary conditions are:
    # - The sum of two values (a[i] and a[j]) is a multiple of 3
    # - The difference between the two values is also a multiple of 3
    # We can derive the maximum number of valid triples for each a[i]
    max_triples = [sum([1 for i in range(n) if (arr[i] - arr[j]) % 3 == 0 and (arr[i] + arr[j]) % 3 == 0]) for j in range(n)]
    return max(max_triples)