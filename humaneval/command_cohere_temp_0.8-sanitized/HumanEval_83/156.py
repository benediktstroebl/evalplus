def starts_one_ends(n):
    # Define a variable to store the answer
    count = 0
    
    # Loop through potential starting digits from 1 to n
    for digit in range(1, n + 1):
        # Determine if the current digit is a potential starting digit
        if digit == 1 or digit == n:
            count += 1
    
    # Return the calculated count
    return count