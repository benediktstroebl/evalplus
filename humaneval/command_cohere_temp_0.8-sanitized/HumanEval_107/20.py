def even_odd_palindrome(n):
    """
    This function takes a positive integer n and returns a tuple containing the count of even and odd integer palindromes in the range(1, n+1).
    
    Args:
        n (int): The upper limit for the range of integers to consider.
    
    Returns:
        tuple: A tuple with two elements: (even_palindrome_count, odd_palindrome_count).
    """
    
    # These are the edge cases, where there is only one integer palindrome possible
    if n == 1:
        return (1, 0)
    if n == 2:
        return (1, 1)
    
    even_count = 0
    odd_count = 0
    
    # We initialize the range of iteration through integers from 1 to n
    for num in range(1, n+1):
        # We check if the integer is a palindrome and update the count accordingly
        if str(num) == str(num)[::-1]:
            if num % 2 == 0:
                even_count += 1
            else:
                odd_count += 1
    
    return (even_count, odd_count)