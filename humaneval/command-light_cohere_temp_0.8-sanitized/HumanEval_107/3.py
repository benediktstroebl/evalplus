def even_odd_palindrome(n):
    """
    Given a positive integer n, return a tuple that has the number of even and odd
    integer palindromes that fall within the range(1, n), inclusive.

    Returns: tuple with the number of even and odd integer palindromes, respectively.
    Input:
        n: Positive integer, parameter.
    Output:
        even: Positive integer, representing the number of even integer palindromes
        odd: Positive integer, representing the number of odd integer palindromes
    """
    # Define a counter for even palindromes
    even_count = 0
    # Define a counter for odd palindromes
    odd_count = 0
    # Loop from 1 to n
    for i in range(1, n + 1):
        # Check if the current integer is even
        if i % 2 == 0:
            even_count += 1
        # Check if the current integer is odd
        else:
            odd_count += 1
    # Return the counts of even and odd integer palindromes
    return (even_count, odd_count)