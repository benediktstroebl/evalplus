
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
    # ------------------- Solution 1
    # time complexity: O(n)
    # space complexity: O(n)
    all_palindromes = list(range(1, n))
    odd_palinds = [x for x in all_palindromes if x % 2 != 0]
    even_palinds = [x for x in all_palindromes if x % 2 == 0]
    return len(odd_palinds), len(even_palinds)
    # ------------------- Solution 2
    # time complexity: O(n)
    # space complexity: O(1)

