
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
    # check if n is even or odd
    if n % 2 == 0:
        even_num = 0
    else:
        even_num = 1

    # check if n is prime or not
    if n == 1:
        is_prime = True
    else:
        is_prime = n > 1 and all(num not in set(range(2, n + 1)) for num in range(2, n + 1))

    # check if n is prime or not
    if is_prime:
        # for i in range(2, n + 1):
            # if n % i == 0:
                # break
        # if break not occur:
            # odd_num += 1
    else:
        odd_num = 0

    # check if n is prime or not
    if n == 2:
        even_num = 2
    elif n == 3:
        even_num = 4
    elif n == 5:
        even_num = 10
    elif n == 7:
        even_num = 14

    # calculate even and odd palindrome of n
    even_palindrome = [2 * i for i in range(1, n + 1)]
    odd_palindrome = [2 * i for i in range(1, n + 1, 2)]

    # return the tuple of even and odd palindrome
    return (even_num, odd_num)
