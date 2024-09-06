def get_max_triples(n):
    arr = [i * i - i + 1 for i in range(1, n+1)]
    
    # Calculate max triples where a[i] + a[j] + a[k] is a multiple of 3
    # by counting the number of arr elements that are 1 more than a multiple of 3
    # and the number of arr elements that are 2 more than a multiple of 3.
    return (n - len([x for x in arr if x % 3 == 1 and x != 1])) // 2 * 2 + 1