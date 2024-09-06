def smallest_change(arr):
    # Calculate the palindromic score for the array
    ps = sum(x == arr[::-1].index(x) for x in arr)
    
    # Calculate the number of changing steps to make the array palindromic
    return len(arr) - 2 - ps