
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
    if n <= 1:
        return (0, 0)

    num_even, num_odd = 0, 0
    # if we know 10^i, we can count how many palindrome numbers below 10^i + 10^i
    # with i digits
    for i in range(1, int(math.log10(n)) + 1):
        base = 10**i
        num_even += 9 * (10**(i - 1)) * (10**(i - 1))
        if i == 1:
            num_odd += 9
        else:
            num_odd += 10 * (10**(i - 1)) * (10**(i - 1))

    # for i digit palindrome numbers, we have 10(i - 1) choices for the left half and
    # 10(i - 1) choices for the right half
    # but we have to remove those that are not smaller than 10^i, so we need to substract
    # (10 - 10**(i - 1)) * (10**(i - 1))
    i = int(math.log10(n))
    num_even += (10**(i - 1)) * (10**(i - 1))
    num_odd -= (10 - 10**(i - 1)) * (10**(i - 1))
    return (num_even, num_odd)

