
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

    # 1. pre-processing
    even_cnt, odd_cnt = 0, 0

    # 2. initiate variables
    left, right = 1, n

    # 3. iterate over the numbers from 1 to n
    for num in range(1, n + 1):

        # 3.1 change the number to a string,
        # and check if the string is a palindrome
        if str(num) == str(num)[::-1]:

            # 3.1.1 if it is, check if the last digit of the string is odd or even
            # to see if it is even or odd
            if num % 2 == 0:
                even_cnt += 1
            else:
                odd_cnt += 1

        # 3.2 check if the numbers are less than or equal to the last palindrome number
        if num <= right:

            # 3.2.1 if it is, check if the last digit of the number is odd or even
            # to see if it is even or odd
            if num % 2 == 0:
                even_cnt += 1
            else:
                odd_cnt += 1

    # 4. return a tuple with the number of even and odd palindromes
    return even_cnt, odd_cnt

