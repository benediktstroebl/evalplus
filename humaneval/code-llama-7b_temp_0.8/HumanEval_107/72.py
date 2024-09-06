
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
    def count_palindrome(n, is_even):
        def count_digit(n):
            cnt = 0
            while n:
                n //= 10
                cnt += 1
            return cnt

        def digit_str(n):
            digit_str = ''
            while n:
                digit_str += str(n % 10)
                n //= 10
            return digit_str

        cnt = 0
        if is_even:
            for i in range(1, n + 1):
                if i == int(digit_str(i)):
                    cnt += 1
        else:
            for i in range(1, n + 1):
                if i == int(digit_str(i)[1:] + digit_str(i)[0]):
                    cnt += 1
        return cnt

    return (count_palindrome(n, True), count_palindrome(n, False))

