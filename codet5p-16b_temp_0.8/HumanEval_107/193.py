
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

    start = 1
    count = 0
    result = [0, 0]

    while start <= n:
        for i in range(start, n+1):
            num = str(i)
            mid = len(num) // 2
            if mid % 2 == 0:
                continue
            if num[:mid] == num[:mid][::-1] and num[mid+1:] == num[mid+1:][::-1]:
                count += 1
                result[0] += 1
            else:
                result[1] += 1

        start *= 10
        count = 0
    
    return tuple(result)
