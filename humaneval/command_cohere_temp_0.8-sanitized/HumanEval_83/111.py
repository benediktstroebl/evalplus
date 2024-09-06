def starts_one_ends(n):
    # Create a list to store the digits
    digits = list(range(1, n + 1))
    
    # Handle the case where n equals 1
    if n == 1:
        return 1
    
    # Handle the case where n equals 2
    if n == 2:
        return 3
    
    # Handle the case where the number is 1 followed by (n-1) zeros
    if n > 2:
        digits.remove(1)
        return starts_one_ends(n - 1) + digits.count(1)
    
    # The base case
    return 0