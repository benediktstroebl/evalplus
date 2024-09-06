
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
    # O(N * logN)
    # space: O(N)

    even, odd = 0, 0
    for i in range(1, n + 1):
        # even
        e_left, e_right = 1, i
        while e_left <= e_right:
            if str(e_left) == str(e_right)[::-1]:
                even += 1
                break
            e_left += 1
        e_left, e_right = 1, int(str(i)[::-1])
        while e_left <= e_right:
            if str(e_left) == str(e_right)[::-1]:
                even += 1
                break
            e_left += 1

        # odd
        o_left, o_right = 1, i
        while o_left <= o_right:
            if str(o_left) == str(o_right)[::-1]:
                odd += 1
                break
            o_left += 1
        o_left, o_right = 1, int(str(i)[::-1])
        while o_left <= o_right:
            if str(o_left) == str(o_right)[::-1]:
                odd += 1
                break
            o_left += 1
    return even, odd


    # O(N)
    # space: O(N)

    # even, odd = 0, 0
    # counter = [0] * (n + 1)
    # for i in range(1, n + 1):
    #     e_left, e_right = 1, i
    #     while e_left <= e_right:
    #         if str(e_left) == str(e_right)[::-1]:
    #             even += 1
    #             if counter[i] == 1:
    #                 counter[i] = 0
    #                 break
    #             else:
    #                 counter[i] = 1
    #             break
    #         e_left += 1
    #     e_
