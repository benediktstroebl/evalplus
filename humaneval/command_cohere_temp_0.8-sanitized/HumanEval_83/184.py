def starts_one_ends(n):
    """
    Given a positive integer n, return the count of the numbers of n-digit
    positive integers that start or end with 1.
    """
    # Create a list to store the digits from 0 to 9.
    digits = list(range(10))
    # Remove the digits 0 and 1 to avoid duplicates when starting or ending with 1.
    digits.remove(0)
    digits.remove(1)
    
    # Consider all n-digit numbers from 2 to 9999...99 (maximum n = 4)
    max_n_digit = max(str(len(str(i))) for i in range(1000, 10000, 2))
    n_digit = int(max_n_digit)
    
    count = 0
    for i in range(2, 10**n_digit):
        current_num = str(i)
        if current_num[0] == '1' or current_num[-1] == '1':
            count += 1
        if len(current_num) == n_digit:
            break
    
    return count