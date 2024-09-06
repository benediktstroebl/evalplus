
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
    # first get the number of even and odd palindromes in the range(1, n)
    # then calculate the sum of all the even and odd palindromes in the range(1, n)
    # lastly subtract the sum of even palindromes from the sum of odd palindromes
    count_of_even_palindromes = 0
    count_of_odd_palindromes = 0
    for i in range(1, n + 1):
        # if we can generate the same number by reversing the digits and converting it to int
        if i == int(str(i)[::-1]):
            count_of_even_palindromes += 1

        # if we can make it by reversing the digits and adding the reversed number
        # and then converting it to int
        if i == int(str(i)[::-1] + str(i)):
            count_of_odd_palindromes += 1

    return count_of_even_palindromes, count_of_odd_palindromes
