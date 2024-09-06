def get_max_triples(n):
    arr = [i * i - i + 1 for i in range(1, n+1)]
    
    # Calculate the maximum number of triples where a[i] + a[j] + a[k] is a multiple of 3.
    # We count the number of triples where the sum is 0, 3, 6, 9, ... , 
    # By factoring out 3, we can simplify this to 0, 1, 2, 3, ... , n-1.
    max_triples = sum(1 for i in range(n) for j in range(i + 1, n) for k in range(j + 1, n) 
                      if (arr[i] + arr[j] + arr[k]) % 3 == 0)
    
    return max_triples