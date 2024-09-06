
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
    # store even and odd count
    counter = [0, 0]

    # loop through all the numbers
    for i in range(1, n+1):
        # get the number of digits
        num_of_digits = len(str(i))

        # check if the number is palindrome
        is_palindrome = i % (10**num_of_digits) == 0

        # check if the number is even or odd
        is_even = i % 2 == 0

        # if the number is palindrome and even, update the even counter
        if is_palindrome and is_even:
            counter[0] += 1
        # if the number is palindrome and odd, update the odd counter
        elif is_palindrome:
            counter[1] += 1

    return counter
