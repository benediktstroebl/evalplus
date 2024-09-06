
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
    #Start with a list of all integers from 1 to n
    numbers = [i for i in range(1,n+1)]
    #create a list of even numbers
    evens = [i for i in numbers if i % 2 == 0]
    #create a list of odd numbers
    odds = [i for i in numbers if i % 2 == 1]
    #count the number of even and odd palindromes
    evens_count = len(set(evens))
    odds_count = len(set(odds))
    return (evens_count, odds_count)
