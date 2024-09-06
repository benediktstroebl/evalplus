
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
    #time complexity O(n)
    #space complexity O(1)
    #Find the number of even and odd palindromes in range(1, n)
    even_palindromes = 0
    odd_palindromes = 0
    for i in range(1, n+1):
        str_i = str(i)
        #If i is an even number, then i + i = 2i is a palindrome
        #If i is an odd number, then i + i = 2i + 1 is a palindrome
        if str_i == str_i[::-1]:
            if i % 2 == 0:
                even_palindromes += 1
            else:
                odd_palindromes += 1
    return (even_palindromes, odd_palindromes)
