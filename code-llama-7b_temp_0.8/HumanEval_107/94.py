
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
    ### Practice:
    def helper(n, odd_even_palindromes, num):
        if num > n:
            return
        if num % 2 == 0:
            odd_even_palindromes[0] += 1
        else:
            odd_even_palindromes[1] += 1
        helper(n, odd_even_palindromes, num + 1)
        return
    odd_even_palindromes = [0, 0]
    helper(n, odd_even_palindromes, 1)
    return odd_even_palindromes

    ### DFS
    def dfs(n, odd_even_palindromes, num):
        if num > n:
            return
        if num % 2 == 0:
            odd_even_palindromes[0] += 1
        else:
            odd_even_palindromes[1] += 1
        dfs(n, odd_even_palindromes, num + 1)
        dfs(n, odd_even_palindromes, num + 1)
        return
    odd_even_palindromes = [0, 0]
    dfs(n, odd_even_palindromes, 1)
    return odd_even_palindromes

    ### Best Practice 1:
    def palindrome(num):
        return [x for x in range(num, 0, -1) if str(x) == str(x)[::-1]]

    def helper(n):
        odd, even = 0, 0
        for i in range(1, n + 1):
            odd += any(x % 2 for x in palindrome(i))
            even += any(not x % 2 for x in palindrome(i))
        return odd, even
    return helper(n)

    ### Best Practice 2:
    def is_palindrome(n):
        return str(n) == str(n)[::-1]

    def helper(n):
        odd, even = 0
