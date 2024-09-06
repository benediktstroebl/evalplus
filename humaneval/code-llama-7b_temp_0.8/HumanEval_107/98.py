
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
    # 翻转一半然后比较 12345678
    # 翻转一半然后比较 1234567
    # 翻转一半然后比较 123456
    # 翻转一半然后比较 12345
    # 翻转一半然后比较 1234
    # 翻转一半然后比较 123
    # 翻转一半然后比较 12
    # 翻转一半然后比较 1
    # 翻转一半然后比较 2
    # 翻转一半然后比较 3
    # 翻转一半然后比较 4
    # 翻转一半然后比较 5
    # 翻转一半然后比较 6
    # 翻转一半然后比较 7
    # 翻转一半然后比较 8
    # 翻转一半然后比较 9
    # 翻转一半然后比较 11
    # 翻转一半然后比较 12

    count = [0, 0]
    for i in range(1, n + 1):
        if is_palindrome(i):
            count[len(str(i)) % 2] += 1
    return count

