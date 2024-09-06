
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
    def palindrome_divisor(num):
        """
        Given a number, how many divisors are it has?
        We use the slow algorithm, 
        This is a recursive algorithm
        """
        divisors = 1
        for i in range(2, num):
            if num % i == 0:
                divisors += 1
        return divisors

    def is_palindrome(num):
        """
        Given a number, if it is a palindrome
        return True, else False
        """
        reverse_num = 0
        temp = num
        while temp:
            reverse_num = reverse_num * 10 + temp % 10
            temp //= 10

        if num == reverse_num:
            return True
        else:
            return False

    count_even = 0
    count_odd = 0

    for num in range(1, n + 1):
        if is_palindrome(num):
            if palindrome_divisor(num) % 2 == 0:
                count_even += 1
            else:
                count_odd += 1
    return (count_even, count_odd)

