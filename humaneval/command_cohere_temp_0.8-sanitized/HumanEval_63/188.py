def fibfib(n):
    # Initialize the cache with first few terms
    cache = [0, 0, 1]
    for i in range(3, n+1):
        cache.append(cache[i-1] + cache[i-2] + cache[i-3])
    return cache[n]