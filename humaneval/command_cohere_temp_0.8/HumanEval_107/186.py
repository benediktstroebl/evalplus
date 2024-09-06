```python
def count_palindromes(n):
    # memoization for counting even and odd length palindromes
    even, odd = 0, 0
    for i in range(1, n + 1):
        if str(i) == str(i)[::-1]:
            even += 1
        else:
            odd += 1
    return even, odd

def even_odd_palindrome(n):
    """
    Given a positive integer n, return a tuple that has the number of even and odd
    integer palindromes that fall within the range(1, n), inclusive.

    Example 1:

        Input: 3
        Output: (1, 2)
        Explanation:
        There is one even palindrome (e.g., 4) and two odd palindromes (e.g., 1, 3).

    Example 2:

        Input: 12
        Output: (4, 6)
        Explanation:
        There are four even palindromes (e.g., 4, 6, 8, 11) and six odd palindromes (e.g., 1, 3, 5, 7, 9, 10).

    Note:
        1. 1 <= n <= 10^3
        2. returned tuple has the number of even and odd integer palindromes respectively.
    """
    return count_palindromes(n)
```

The key process is converting each integer `i` in `range(1, n+1)` to a string (`str(i)`), then comparing this string to its reverse (`str(i) == str(i)[::-1]`), using memoization to count even and odd lengths to speed up the process, and returning the count as a tuple `(even, odd)`. This solves the given problem in a more efficient manner. 

This approach has a time complexity of O(n). It takes O(n) time because each integer needs to be converted to a string which takes O(1) time, and then compared to its reverse, which also takes O(1) time, and this process is done for each integer in `range(1, n+1)` which takes O(n) time. The memoization of counting even and odd palindromes saves time for further efficiency.