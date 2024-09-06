
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
    # create a list of numbers from 1 to n
    numbers = list(range(1, n + 1))
    # filter even numbers
    even_numbers = [num for num in numbers if num % 2 == 0]
    # filter odd numbers
    odd_numbers = [num for num in numbers if num % 2 == 1]
    # count the number of even and odd numbers that are also palindromes
    even_palindrome = len(filter(lambda x: x % 2 == 0 and x == x[::-1], even_numbers))
    odd_palindrome = len(filter(lambda x: x % 2 == 1 and x == x[::-1], odd_numbers))
    return (even_palindrome, odd_palindrome)

