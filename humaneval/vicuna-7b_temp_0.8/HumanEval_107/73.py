
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
    # Creating a set to store even and odd numbers
    even_set = set()
    odd_set = set()
    # Creating a dictionary to store the number of even and odd palindromes
    count = {}
    # Iterating through the range of 1 to n
    for i in range(1, n+1):
        # Checking if the number is even or odd
        if i % 2 == 0:
            even_set.add(i)
            count[(i, 1)] = count[(i, 1)] + 1
            count[(i, -1)] = count[(i, -1)] + 1
        else:
            odd_set.add(i)
            count[(i, 1)] = count[(i, 1)] + 1
    # Removing the even numbers that have an odd number of palindromes
    for key in count:
        count[key] = count[key] - odd_set.difference(even_set)
    # Removing the odd numbers that have an even number of palindromes
    for key in count:
        count[key] = count[key] - even_set.difference(odd_set)
    return count
