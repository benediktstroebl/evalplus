
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
    # we can use string to solve this problem, as we can only generate palindromes
    # of size 3 or 5
    # construct two strings, one is '1234', another is '54321'
    # '54321' starts with one 5, so it cant be a palindrome
    # since we can only generate palindromes of size 3 and 5, so the palindrome should
    # be a multiple of 3, 3, 6, or 9
    # now we can check if the first and last element of the strings are the same, which is
    # a palindrome
    # we can use O(1) extra space to store the last digit of each string
    # we can use O(1) extra space to keep track of the last occurence of the current
    # digit
    # use the first occurence of the current digit as the first item in the palindrome,
    # and the last occurence of the current digit as the last item in the palindrome
    # we can keep a running tally of the last occurence of each digit, and when we see a
    # new digit, we add to the running tally
    # we can also keep a running tally of the odd and even occurance, so we can return them

    odd_count = even_count = 0
    # odd_count tracks number of odd-length palindromes
    # even_count tracks number of even-length palindromes
    last_digit = 0
    last_digit_odd = last_digit_even = 0
    for i in xrange(1, n+1):
        # expect the first and last digits to be the same
        # ex. 54321, so the first and last digits should be 5
        digit = (i / 10) % 10
        if i < 10:
            last_digit = i
        else:
            # update the last digit
            last_digit = (i / 10) % 10
            last_digit_odd += (i / 10) % 10
            last_digit_even += (i / 10) % 10

        # first condition is when the last digit is the same as first digit
        # second condition is when the last digit is the same as the first digit in