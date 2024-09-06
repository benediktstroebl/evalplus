
def get_odd_collatz(n):
    """
    Given a positive integer n, return a sorted list that has the odd numbers in collatz sequence.

    The Collatz conjecture is a conjecture in mathematics that concerns a sequence defined
    as follows: start with any positive integer n. Then each term is obtained from the 
    previous term as follows: if the previous term is even, the next term is one half of 
    the previous term. If the previous term is odd, the next term is 3 times the previous
    term plus 1. The conjecture is that no matter what value of n, the sequence will always reach 1.

    Note: 
        1. Collatz(1) is [1].
        2. returned list sorted in increasing order.

    For example:
    get_odd_collatz(5) returns [1, 5] # The collatz sequence for 5 is [5, 16, 8, 4, 2, 1], so the odd numbers are only 1, and 5.
    """

    # 建立積存空間
    cache = {}
    # 將輸入數輸出存入積存空間
    cache[n] = [n]
    # 從輸入數開始，進行迴圈檢查
    while n != 1:
        # 若積存空間含有n時，則直接取得該積存空間的list，並將其重新存入積存空間
        if n in cache:
            cache[n] = cache[n] + cache[n // 2 + 1] if n % 2 == 0 else cache[n // 2 + 1] + [n]
        # 若積存空間不含有n時，進入迴圈
        else:
            # 若n為偶數，則積存空間存入1，並繼續迴圈
            if n % 2 == 0:
                cache[n] = cache[n // 2 + 1] + [1]
            # 若n為奇數，則積存空間存入3n + 1，並繼續迴圈
            else:
                cache[n] = cache[3 * n + 1] + [n]
        # 更新n
        n = cache[n][-1]
    # 回傳積存空間中的list
    return cache[1]

