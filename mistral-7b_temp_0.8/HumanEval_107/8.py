
def even_odd_palindrome(n):
    """
    Given a positive integer n, return a tuple that has the number of even and odd
    integer palindromes that fall within the range(1, n), inclusive.

    Example 1:

        Input: 3
        Output: (1, 2)
        Explanation:
        Integer palindrome are 1, 2, 3. one of them is even, and two of them are odd.

    Example 2:

        Input: 12
        Output: (4, 6)
        Explanation:
        Integer palindrome are 1, 2, 3, 4, 5, 6, 7, 8, 9, 11. four of them are even, and 6 of them are odd.

    Note:
        1. 1 <= n <= 10^3
        2. returned tuple has the number of even and odd integer palindromes respectively.
    """
    # Initialize even and odd counters
    even_count = 0
    odd_count = 0

    # Iterate over the range [1, n]
    for i in range(1, n + 1):
        # Check if i is a palindrome
        palindrome = True
        for j in range(len(str(i)) // 2):
            if str(i)[j] != str(i)[-j - 1]:
                palindrome = False
                break
        # If i is a palindrome and even, increment even count
        if palindrome and i % 2 == 0:
            even_count += 1
        # If i is a palindrome and odd, increment odd count
        elif palindrome and i % 2 != 0:
            odd_count += 1

    # Return the tuple with even and odd counts
    return even_count, odd_count
