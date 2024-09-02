
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
    # Using a list to count the number of even and odd palindromes
    count_list = [0, 0]
    # Iterating through the range of n
    for i in range(1, n+1):
        # Checking if the number is a palindrome
        if i == int(i):
            count_list[i % 2 == 0].append(i)
    # Extracting the even palindromes
    even_palindromes = [x[0] for x in count_list if x[0] > 0]
    # Extracting the odd palindromes
    odd_palindromes = [x[0] for x in count_list if x[0] == 0]
    # Returning the tuple of even and odd palindromes
    return (len(even_palindromes), len(odd_palindromes))
