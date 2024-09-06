def get_max_triples(n):
    arr = [i * i - i + 1 for i in range(1, n+1)]
    
    # Calculate max triples where a[i] + a[j] + a[k] is a multiple of 3
    # By condition, either a[i] or a[j] or a[k] is a multiple of 3
    # Therefore, 3 divides a[i]-1, or 3 divides a[j]-1 or 3 divides a[k]-1
    # So 2*3 divides (a[i]-1 + a[j]-1 + a[k]-1) = (a[i]+a[j]+a[k])-3
    max_triples = len(arr) * (len(arr) - 1) // 2
    
    return max_triples