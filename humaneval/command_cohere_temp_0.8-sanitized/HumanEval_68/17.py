def pluck(arr):
    if not arr:
        return []
    
    # Using collections.Counter to efficiently find the smallest even value and its index
    # Counter remembers the first occurrence of an element, ensuring we get the node with the smallest index
    min_value, min_index = (min(x for x, i in collections.Counter(arr).items() if x % 2 == 0),
                            next(i for x, i in collections.Counter(arr).items() if x % 2 == 0))
    
    return [min_value, min_index]