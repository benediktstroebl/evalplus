
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
    assert 1 <= n <= 10**3
    if n == 1:
        return (1, 0)

    # # way too slow (the O(n^2) solution)
    # even = 0
    # odd = 0
    # for i in range(1, n):
    #     for j in range(i, n+1):
    #         word = str(i) + str(j)[::-1]
    #         if is_palindrome(word):
    #             if word % 2 == 0:
    #                 even += 1
    #             else:
    #                 odd += 1
    # return (even, odd)

    even = [0 for _ in range(n)]
    odd = [0 for _ in range(n)]
    for i in range(1, n):
        for j in range(i, n+1):
            word = str(i) + str(j)[::-1]
            if is_palindrome(word):
                if word % 2 == 0:
                    even[i-1] += 1
                else:
                    odd[i-1] += 1
    return (sum(even), sum(odd))

