
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
    from collections import Counter

    def count_palindromic_odd_even(a):
        even = 0
        odd = 0
        for i in range(1, a + 1):
            if i <= 10:
                if i % 2 == 0 and str(i) == str(i)[::-1]:
                    even += 1
                elif i % 2!= 0 and str(i) == str(i)[::-1]:
                    odd += 1
            else:
                i = str(i)
                if int(i) % 2 == 0 and i == i[::-1]:
                    even += 1
                elif int(i) % 2!= 0 and i == i[::-1]:
                    odd += 1
        return even, odd

    result = Counter()
    for i in range(1, n + 1):
        even, odd = count_palindromic_odd_even(i)
        result[i] = (even, odd)
    return result

