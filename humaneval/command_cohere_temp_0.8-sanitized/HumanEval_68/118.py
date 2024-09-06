def pluck(arr):
    if not arr:
        return []
    
    # Using collections.counter to efficiently find the smallest even value and its index
    even_value = min((k for k, v in collections.Counter(arr).items() if v & 1 == 0), key=lambda x: (x, arr.index(x)))
    return [even_value, arr.index(even_value)]