
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

    start, end = 1, n
    start_even, end_even = 0, 0
    for i in range(start, end + 1):
        if i == 1:
            start_even, end_even = 1, 1
            continue
        if i % 2 == 0:
            curr = i
            rev = int(str(curr)[::-1])
            if curr == rev:
                start_even += 1
            if rev >= start and rev <= end:
                end_even += 1
        else:
            curr = i
            rev = int(str(curr)[::-1])
            if curr == rev:
                start_even += 1
            if rev >= start and rev <= end:
                end_even += 1
    curr = start
    rev = int(str(curr)[::-1])
    if curr == rev:
        start_even += 1
    if rev >= start and rev <= end:
        end_even += 1
    return (start_even, end_even)
