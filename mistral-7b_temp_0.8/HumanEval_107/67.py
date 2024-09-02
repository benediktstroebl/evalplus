
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
    def is_palindrome(num):
        '''
        Return true if the input number is a palindrome.
        '''
        if num < 0:
            return False
        s = str(num)
        return s == s[::-1]

    def is_even(num):
        '''
        Return true if the input number is even.
        '''
        return num % 2 == 0

    count_even = 0
    count_odd = 0

    for num in range(1, n+1):
        if is_palindrome(num):
            if is_even(num):
                count_even += 1
            else:
                count_odd += 1

    return count_even, count_odd
