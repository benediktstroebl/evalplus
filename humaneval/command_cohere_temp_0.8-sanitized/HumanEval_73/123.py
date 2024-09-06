def smallest_change(arr):
    # Count the number of occurring elements
    occur = dict()
    for num in arr:
        if num in occur:
            occur[num] += 1
        else:
            occur[num] = 1
    
    # Calculate the required changes
    changes = 0
    for num, count in occur.items():
        if count % 2 == 1:
            changes += 1
    
    return changes