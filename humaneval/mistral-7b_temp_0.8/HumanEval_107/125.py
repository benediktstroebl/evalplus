
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
    # Palindrome generator.
    def gen_palindrome(x):
        """
        Given an integer x, return an iterator for an infinite sequence of integer palindromes
        that are strictly greater than x.
        """
        # The list of all possible digits of a palindrome.
        digit_pool = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
        # The rest of digits are used to count number of palindrome.
        digit_pool_count = len(digit_pool)
        # The last digit of a palindrome.
        last_digit = '0'
        # The number of digits in a palindrome.
        number_of_digits = 1

        # Generate palindromes.
        def gen_palindrome():
            nonlocal last_digit, number_of_digits
            for digit in digit_pool:
                last_digit = digit
                for _ in range(number_of_digits):
                    yield
