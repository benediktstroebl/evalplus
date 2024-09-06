def get_max_triples(n):
    arr = [i * i - i + 1 for i in range(1, n+1)]
    
    # Calculate max triples where a[i] + a[j] + a[k] is a multiple of 3
    # By observing that the necessary condition is that the sum of two adjacent elements is multiple of 3,
    # we can split the array into cycles and sum two adjacent elements in each cycle.
    cycles = arr[:]
    for i in range(len(arr)):
        if arr[i] + arr[i+1] % 3 == 0:
            cycles[i] = arr[i] + arr[i+1]
        elif arr[i] + arr[i-1] % 3 == 0:
            cycles[i] = arr[i-1] + arr[i]
        else:
            cycles[i] = max(arr[i-1] + arr[i], arr[i] + arr[i+1])
    
    # Count the number of cycles
    # (we have 3 * cycles.count() - 2 * len(arr) + 1 triples in total)
    triple_cycles = 0
    for i in range(len(cycles)):
        if cycles[i] != 0:
            triple_cycles += 1
    return (3 * triple_cycles - 2 * len(arr) + 1) // 3