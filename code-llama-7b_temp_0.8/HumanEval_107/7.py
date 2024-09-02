
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
    if n < 1:
        raise ValueError('n must be >= 1')
    if n > 10**3:
        raise ValueError('n must be <= 10**3')

    # Initialize variables
    even_num = 0
    odd_num = 0

    for number in range(1, n+1):
        num_str = str(number)

        if len(num_str) % 2 != 0:
            # Odd number of digits
            for i in range(0, int((len(num_str) + 1) / 2)):
                if num_str[i] != num_str[len(num_str) - 1 - i]:
                    break
            else:
                # It is a palindrome
                if number % 2 == 0:
                    even_num += 1
                else:
                    odd_num += 1
        else:
            # Even number of digits
            for i in range(0, int(len(num_str) / 2)):
                if num_str[i] != num_str[len(num_str) - 1 - i]:
                    break
            else:
                # It is a palindrome
                if number % 2 == 0:
                    even_num += 1
                else:
                    odd_num += 1

    return (even_num, odd_num)

