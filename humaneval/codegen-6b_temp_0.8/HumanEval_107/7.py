
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
    even, odd = 0, 0

    # ctr is used to count number of cubes of odd and even digits
    ctr = 1
    while ctr <= n:
        # for each range of digits, it keeps track of the number of cubes
        # of odd and even digits as well as the number of palindromes
        # that can be formed between these two digits.
        odd_dig, odd_pal = 1, 0
        even_dig, even_pal = 1, 0

        # digit has to be less than 10, because we cannot have cubes
        # of digits higher than 10
        while n // (10 ** (ctr - 1)) > 0:

            # cubed digit is the n // (10 ** (ctr - 1))
            cubed_dig = n // (10 ** (ctr - 1))

            # pattern of numbers between digits that are palindromes
            # formed by the cubed digits
            pal = str(cubed_dig ** 3)
            pal_len = len(pal)

            # if cubed digit is an odd integer, increment number of odd
            # palindromes, increment number of cubes of odd digits and
            # update number of digits
            if cubed_dig % 2 == 1:
                odd_dig += 1
                odd_pal += pal_len
                n -= cubed_dig

            # if cubed digit is an even integer, increment number of even
            # palindromes, increment number of cubes of even digits and
            # update number of digits
            else:
                even_dig += 1
                even_pal += pal_len
                n -= cubed_dig

            # move to next digit
            ctr += 1

        # update even and odd palindrome counts
        even += even_dig * even_pal
        odd += odd_dig * odd_pal

    return even, odd


assert even_odd_palindrome(3) == (1, 2)
assert even_odd_palindrome(12) == (4, 6)
assert even_odd_palindrome(100) == (49, 50)
