
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
    # idea: step 1: enumerate all palindromes upto n
    # step 2: check if n-digit palindrome is an even or odd palindrome
    # time complexity: each step is O(n)
    # space complexity: O(n)
    # use 2 pointers, i and j
    # i records the last index that is a digit
    # j records the last index that is not a digit
    # j starts from the end of each palindrome, i starts from the begining
    # when i < j
    # if count is odd, j is on the right side of i
    # if count is even, i is on the left side of j
    # always count j-i is odd
    # increase both i and j
    # if (i == j) => n-digit palindrome is an even integer palindrome
    # if (i < j) => n-digit palindrome is an odd integer palindrome
    def is_palindrome(num):
        s = str(num)
        return s == s[::-1]

    if n < 10:
        return (1, 1) if n % 2 == 0 else (1, 0)

    even, odd = 0, 0
    i, j = 0, 1
    while j < n:
        while i < n and not is_palindrome(i):
            i += 1
        while j < n and not is_palindrome(j):
            j += 1
        while j < n and is_palindrome(j):
            j += 1
        while i < n and is_palindrome(i):
            even += 1
            i += 1
        while j < n and is_palindrome(j):
            odd += 1
            j += 1
    return (even, odd)
