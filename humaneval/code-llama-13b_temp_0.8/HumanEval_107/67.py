
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

    even_count, odd_count = 0, 0
    for i in range(1, n):
        if i % 10 == 0 and i != 0:
            continue

        # Initialize even and odd palindromes for every iteration
        even_palindrome, odd_palindrome = 0, 0

        # Split the number into digits
        digit = [int(x) for x in str(i)]
        digit_len = len(digit)

        # Base case
        if digit_len == 1:
            even_palindrome = 1
            odd_palindrome = 1

        # Split the number into left and right halves
        left, right = digit[:digit_len // 2], digit[digit_len // 2:][::-1]
        if left == right:
            even_palindrome += 1

        # Remove the left half and try to reverse the remaining half
        left.pop()
        if left == right[::-1]:
            odd_palindrome += 1

        # Accumulate the number of palindromes for the current iteration
        even_count += even_palindrome
        odd_count += odd_palindrome

    return even_count, odd_count
