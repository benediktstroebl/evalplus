
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
    # cnts = [0 for i in range(n+1)]
    # for i in range(10, n+1):
    #     cnts[i] = cnts[i//10] + 1
    # return cnts[n]
    cnts = [0 for i in range(n+1)]
    for i in range(1, n+1):
        cnts[i] = cnts[i//10]
        if i % 10 == 0:
            cnts[i] -= 1
            if i // 10 > 1:
                cnts[i] += 1
        elif i % 10 % 2 == 0:
            cnts[i] += 1

    return cnts[n], n - cnts[n]

