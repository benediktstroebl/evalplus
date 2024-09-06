def solve(n):
    """
    :type n: int
    :param n: integer
    :rtype: str
    """
    s = str(n)
    return ''.join([str(int(s) + int(s[1:])), '0'][s[0] != '1']).rjust(len(s), '0')