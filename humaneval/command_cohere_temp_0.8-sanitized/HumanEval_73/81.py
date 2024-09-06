def smallest_change(arr):
    # Calculate the palindrome score for the array
    ps = sum(x == arr[::-1].index(x) for x in arr)
    
    # Calculate the inverse palindrome score
    ip = sum(x == arr[::-1].index(x) for x in arr[::-1])
    
    return ps - ip