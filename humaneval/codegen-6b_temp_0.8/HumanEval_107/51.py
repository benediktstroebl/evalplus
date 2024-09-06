
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
    if n == 1:
        return (0, 1)

    # create a string of numbers starting from n
    s = str(n)
    # keep only even and odd digits out of this string
    evens, odds = [], []
    for i in range(0, len(s), 2):
        evens.append(s[i])
    for i in range(1, len(s), 2):
        odds.append(s[i])

    # solve the previous problems with each substring of s
    even, odd = [], []
    for i in range(len(evens), 0, -2):
        even.append(int(evens[i-2:i]))
        a = int(evens[i-1:i+1])
        if a % 2 == 0:
            even.append(a)
    for i in range(len(odds), 0, -2):
        odd.append(int(odds[i-2:i]))
        a = int(odds[i-1:i+1])
        if a % 2 == 1:
            odd.append(a)

    total_even, total_odd = 0, 0
    for e in even:
        if e == e[::-1]:
            total_even += 1
    for o in odd:
        if o == o[::-1]:
            total_odd += 1
    return (total_even, total_odd)

