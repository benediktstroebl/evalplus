
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
    from collections import deque
    queue = deque([str(i) for i in range(1,n+1)])
    even_count = 0
    odd_count = 0
    while queue:
        head = queue.popleft()
        if len(head)==1:
            if head=='1':
                even_count+=1
            elif head=='3':
                odd_count+=1
        elif len(head)==2:
            if head=='11':
                even_count+=1
            elif head=='33':
                odd_count+=1
        elif len(head)==3:
            if head=='111':
                even_count+=1
            elif head=='333':
                odd_count+=1
        else:
            if head=='1111':
                even_count+=1
            elif head=='3333':
                odd_count+=1

        # since we cannot reverse negative numbers
        if int(head)<0:
           
