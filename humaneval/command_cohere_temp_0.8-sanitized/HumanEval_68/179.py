from sortedcontainers import SortedSet
def pluck(arr):
    even, odd = SortedSet(), SortedSet()
    for i, n in enumerate(arr):
        if n % 2 == 0:
            even.add(n)
        else:
            odd.add(n)
    
    if even:
        return [min(even), even.bisect_left(min(even))]
    elif odd:
        return [min(odd), odd.bisect_left(min(odd))]
    else:
        return []