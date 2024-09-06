
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
    # Initialise odd and even count
    count_even = 0
    count_odd = 0
    # Iterate through numbers
    for i in range(1, n+1):
        # If even
        if (i % 2 == 0):
            # Count even numbers as palindrome
            count_even += 1
        else:
            # Count odd numbers as palindrome
            count_odd += 1
        # Keep track of number of digits
        number_of_digits = 1
        # Get the number of digits in number
        while (i > 9):
            number_of_digits += 1
            i //= 10
        # Reverse number
        reverse_number = i
        # Iterate through digits in number
        for j in range(number_of_digits-1):
            # If even
            if ((reverse_number % 10) % 2 == 0):
                # Count even numbers as palindrome
                count_even += 1
            else:
                # Count odd numbers as palindrome
                count_odd += 1
            reverse_number //= 10
    return (count_even, count_odd)
