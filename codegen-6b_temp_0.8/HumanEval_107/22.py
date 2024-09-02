
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
    def count_palindrome_length(x):
        # count the length of the palindromes
        count = 0
        power = len(str(x)) // 2
        for i in range(10 ** power):
            if str(x)[i] != str(x)[-(i+1)]:
                # only count the middle number
                count += 1
        return count

    count_dict = {}
    for i in range(1, n + 1):
        count_dict[i] = count_palindrome_length(i)
    return (count_dict[i] for i in [2] if i % 2 == 1 and count_dict[i] % 2 == 0)

