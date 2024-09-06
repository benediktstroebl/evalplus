def pluck(arr):
    even, odd = partition_by_parity(arr)
    return smallest_element([x + len(odd) for x, y in enumerate(even) if y == min(even)],
                            [x + len(odd) for x, y in enumerate(odd) if y == min(odd)])
def partition_by_parity(arr):
    return even_list(arr), odd_list(arr)
def even_list(arr):
    return [x for x in arr if x % 2 == 0]
def odd_list(arr):
    return [x for x in arr if x % 2 != 0]
def smallest_element(even, odd):
    if not even and not odd:
        return []
    if even:
        return [min(even), min(even.index(min(even)), len(even))]
    return [min(odd), min(odd.index(min(odd)), len(odd))]