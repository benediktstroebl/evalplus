
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

    # Counts the number of odd and even numbers in the given range.
    def count_even_and_odd_palindromes(n):
        count_odd = 0
        count_even = 0

        # Iterate through all the numbers in the range.
        for i in range(1, n + 1):
            # Check if the number is a palindrome.
            if is_palindrome(i):
                # Check if the number is even.
                if i % 2 == 0:
                    count_even += 1
                else:
                    count_odd += 1

        return count_even, count_odd

    # Returns True if the given number is a palindrome, False otherwise.
    def is_palindrome(number):
        # Convert the number to a string.
        number = str(number)
        # Iterate through the string from the beginning and end.
        for i in range(len(number) // 2):
            # Check if the characters at the beginning and end are the same.
            if
