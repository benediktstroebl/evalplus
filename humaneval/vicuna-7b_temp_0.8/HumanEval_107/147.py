
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
    # Create a list of range(1, n) numbers
    numbers = list(range(1, n + 1))
    # Create a list of numbers in reverse order
    numbers_rev = [n]
    # Iterate through numbers
    for num in numbers:
        # Get the number in the range(1, n) that comes before num in the sorted order
        num_prev = numbers[0][:-1]
        # Check if num and num_rev are palindromes
        if num == num_prev:
            # Check if num is even or odd
            if num % 2 == 0:
                even += 1
            else:
                odd += 1
        else:
            even = 0
            odd = 0
        numbers_rev.insert(0, num_prev)
    return (even, odd)