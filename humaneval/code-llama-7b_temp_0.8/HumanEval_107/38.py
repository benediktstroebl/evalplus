
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
    # initialize our even and odd counts
    evens, odds = 0, 0

    # track the start and end of our range
    start, end = 1, n

    # outer loop over the number of digits
    for _ in range(len(str(n))):
        # inner loop over all odd and even ints within the range
        for i in range(start, end + 1, 2):
            # check if i is a palindrome
            if is_palindrome(i):
                # if even, increment our count
                if i % 2 == 0:
                    evens += 1
                # if odd, increment our count
                else:
                    odds += 1

        # adjust our range to be half as large
        start, end = end - start + 1, end

    # return the tuple with the counts
    return evens, odds

