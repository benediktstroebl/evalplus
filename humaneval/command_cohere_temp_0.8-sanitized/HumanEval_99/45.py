def closest_integer(s):
    '''
    Return the closest integer to the given value, rounding away from zero.

    Args:
        s (str): A string representing a number.

    Returns:
        int: The closest integer to the given value.
    '''
    n = float(s)
    dp = [n, n]
    mod = n % 1
    if mod == 0:
        return int(n)
    for i in range(1, 51):
        x = i * 10
        y = x + 1
        if x <= n < y:
            dp[1] = y
        elif x >= n > y:
            dp[0] = x
        elif n == x or n == y:
            continue
        else:
            mid = (x + y) / 2
            if n - mid >= 0:
                dp[1] = y
            else:
                dp[0] = x
    if dp[1] > dp[0]:
        return int(dp[1])
    else:
        return int(dp[0])