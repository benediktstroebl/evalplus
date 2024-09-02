
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
    # initialize the count of each palindrome types
    even, odd = 0, 0
    # max value of the string length
    max_len = len(str(n))
    # iterate over the length of the string
    for i in range(1, max_len+1):
        # iterate over all the number in the range
        for j in range(10**(i-1), 10**i):
            # convert the number to string
            num = str(j)
            # if the first and the last character are the same
            if num[0] == num[-1]:
                # if the number has an even number of characters
                if len(num) % 2 == 0:
                    # count as an even integer palindrome
                    even += 1
                else:
                    # if the number has an odd number of characters
                    # get the middle character
                    mid = num[(len(num)-1)//2]
                    # if the middle character is not the same as the first and the last
                    if mid != num[0] and mid != num[-1]:
                        # count as an odd integer palindrome
                        odd += 1
    # return the tuple with the counts
    return even, odd

