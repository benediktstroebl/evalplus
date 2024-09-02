
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
    # use a hash table to record the occurrence
    # for example, for 12
    # e = 1 2 3 4 5 6
    # o = 7 8 9 11
    # so the return value should be (6, 4)
    ret = {
        'e': 0,
        'o': 0,
    }
    n_range = list(range(1, n + 1))
    for num in n_range:
        num_str = str(num)
        num_len = len(num_str)
        for i in range(num_len):
            if i == num_len - 1:
                ret['o'] += 1
            else:
                if num_str[i] == num_str[-i - 1]:
                    if i + 2 < num_len:
                        ret['e'] += 1
                    else:
                        ret['o'] += 1
                else:
                    break
    return ret['e'], ret['o']
