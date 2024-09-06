def pluck(arr):
    if not arr:
        return []
    
    # Use a default dictionary initialization to quickly find the smallest even value
    d = dict()
    for i, num in enumerate(arr):
        if num % 2 == 0 and (not d or num < d.get('value', float('inf'))):
            d['value'] = num
            d['index'] = i
    if not d:
        return []

    # If there are multiple nodes with the same smallest even value, return the one with the smallest index
    return [d['value'], d['index']]