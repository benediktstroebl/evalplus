
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
    if n <= 1000000:
        # check for even palindromes
        count_even = 0
        for i in range(1, n+1):
            if n % i == 0:
                count_even += 1
                if n // i == i // n:
                    count_even += 1
        return (count_even,)
    elif n <= 10000000000:
        # check for odd palindromes
        count_odd = 0
        for i in range(1, n+1):
            if n % i == 0:
                count_odd += 1
                if n // i == i // n:
                    count_odd += 1
        count_even = (count_odd // 2 + 1) // 2
        return (count_odd, count_even)
    else:
        return (0, 0)
