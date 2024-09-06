def starts_one_ends(n):
    # Create a list to store the digits
    digits = list(range(1, n + 1))
    
    # Handle the edge case where n = 1
    if n == 1:
        return 1
    
    # Handle the case where the number ends with 1
    ends_with_1 = [digit for digit in digits if digit == 1]
    
    # Remove the last digit and handle the case where the number starts with 1
    starter_1 = [digit for digit in digits if digit == 1][:n - 1]