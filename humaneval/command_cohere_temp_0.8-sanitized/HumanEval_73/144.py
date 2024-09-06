def smallest_change(arr):
    # Count the number of occurring elements
    occurring = {}
    for num in arr:
        if num in occurring:
            occurring[num] += 1
        else:
            occurring[num] = 1
    
    # Calculate the required changes
    changes = 0
    for num, count in occurring.items():
        if count % 2 == 1:
            changes += 1
    
    return changes