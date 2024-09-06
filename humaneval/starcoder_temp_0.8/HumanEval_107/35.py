
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

    # init data
    num_even, num_odd = 0, 0
    n_digits = len(str(n))
    limit = 10 ** n_digits

    # i_lower: start index of a integer palindrome in range(1, limit)
    # i_upper: end index of a integer palindrome in range(1, limit)
    # even_upper: upper bound of the even palindrome number
    # odd_upper: upper bound of the odd palindrome number
    for i_lower in range(1, limit):
        i_upper = i_lower
        even_upper = i_lower
        odd_upper = i_lower
        while i_lower <= i_upper <= limit:
            i = int(str(i_lower)[::-1])
            i_upper *= 10
            if i > i_upper - i_lower:
                i_upper = i_upper - i_lower
            else:
                i_upper -= i_lower

            if i_lower <= i <= i_upper <= limit:
                if i % 2 == 0:
                    even_upper = i_upper
                else:
                    odd_upper = i_upper

            i_lower *= 10
        num_even += (even_upper - i_lower + 1)
        num_odd += (odd_upper - i_lower + 1)

    return num_even, num_odd
