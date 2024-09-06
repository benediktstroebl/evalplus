def get_max_triples(n):
    arr = [i * i - i + 1 for i in range(1, n+1)]
    
    # Calculate max triples where a[i] + a[j] + a[k] is a multiple of 3
    # by considering all possible triples with elements in the array
    # and an offset of 2, 5, 8, ... (which are multiples of 3)
    return max(sum(1 for i in range(n) if arr[i] + offset == arr[i] or offset == arr[i] for offset in multiples_of_3(arr[0]))
               for multiples_of_3 in itertools.filtershare(multiples_of_3(0), 2))