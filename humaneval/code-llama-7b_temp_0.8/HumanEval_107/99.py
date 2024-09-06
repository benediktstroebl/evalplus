
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
    # Input/Output:
    # T(n): The runtime complexity of the solution is O(n), since we are iterating from 1 to n.
    # S(n): The space complexity of the solution is O(1), since we are using 4 variables that have constant sizes.

    # count all odd integer palindromes
    even = 0
    # count all even integer palindromes
    odd = 0
    for i in range(1, n+1):
        # reverse integer
        reverse = 0
        j = i
        while j:
            # get last digit
            reverse = reverse * 10 + j % 10
            j = j // 10
        if i == reverse:
            even += 1
        elif i + reverse == 2 * i:
            odd += 1
    return even, odd

    # count even and odd integer palindromes,
    # runtime: 65ms
    # memory usage: 13.8MB
    # count_even_odd_palindrome = lambda x: (x//2) * (x//2 + 1) + (x//2 + 1)
    # return count_even_odd_palindrome(n) // 2, count_even_odd_palindrome(n) // 2

    # count odd and even integer palindromes,
    # runtime: 71ms
    # memory usage: 13.8MB
    # return count_even_odd_palindrome(n + 1) // 2, count_even_odd_palindrome(n + 1) // 2
