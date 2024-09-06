from typing import List


def string_xor(a: str, b: str) -> str:
    """ Input are two strings a and b consisting only of 1s and 0s.
    Perform binary XOR on these inputs and return result also as a string.
    >>> string_xor('010', '110')
    '100'
    """
    ans = ""
    dp = 0
    for i in range(len(a)):
        if a[i] == "1":
            dp += 1
        else:
            dp += 2
    for j in range(len(b)):
        if b[j] == "1":
            dp += 1
        else:
            dp += 2
    for i in range(len(a)):
        for j in range(len(b)):
            if i == j:
                ans += str(dp)
            else:
                ans += str(dp + 1)
                ans += str(gcd(i, j))
                dp = gcd(i, j)
    return ans
