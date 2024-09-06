
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
    # Check if n is positive integer
    if not n > 0:
        return -1

    # Initialize a list to store the number of even and odd palindromes
    even_odd = [0, 0]

    # Loop through range(1, n)
    for i in range(1, n + 1):
        # Initialize a list to store the numbers of the form x*2^k, x*2^k + 1
        x_2 = [int(x) * 2 for x in str(i)]
        x_2_1 = [int(x) * 2 + 1 for x in str(i)]

        # Loop through the numbers in x_2 and x_2_1
        for x in x_2:
            if x % 2 == 0:
                even_odd[0] += 1
            else:
                even_odd[1] += 1

        # Check if there are any odd palindromes
        odd_palindrome = [x for x in x_2_1 if x == int(x) // 2]
        if odd_palindrome:
            even_odd[1] += len(odd_palindrome)

    # Return the tuple
    return (even_odd[0], even_odd[1])
