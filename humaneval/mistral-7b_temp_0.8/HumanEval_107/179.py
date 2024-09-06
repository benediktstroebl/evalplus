
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
    # initialize 2 sets
    even = set()
    odd = set()
    # iterate through range
    for i in range(1, n + 1):
        # iterate through each number
        for j in range(1, i + 1):
            # convert it to a string
            num = str(i)
            # if the reverse is same as the original
            if num == num[::-1]:
                # append to the respective set
                if i % 2 == 0:
                    even.add(i)
                else:
                    odd.add(i)

    # return the number of elements in the set
    return len(even), len(odd)


