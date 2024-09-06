
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
        return (0, 0)

    even, odd = 0, 0
    n_str = str(n)
    if n_str == n_str[::-1]:
        even += 1
        odd += 1
    else:
        odd += 1

    nums = [int(i) for i in str(n)]
    for i in range(len(nums) - 1):
        for j in range(i + 1, len(nums)):
            num_i = nums[i]
            num_j = nums[j]

            new_nums = [int(i) for i in str(num_i * 10 + num_j)]

            if new_nums == new_nums[::-1]:
                if i == j:
                    even += 1
                else:
                    odd += 1
            else:
                odd += 1

    return (even, odd)
