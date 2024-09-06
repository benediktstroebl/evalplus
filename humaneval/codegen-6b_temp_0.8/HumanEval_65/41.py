
def circular_shift(x, shift):
    """Circular shift the digits of the integer x, shift the digits right by shift
    and return the result as a string.
    If shift > number of digits, return digits reversed.
    >>> circular_shift(12, 1)
    "21"
    >>> circular_shift(12, 2)
    "12"
    """
    length = len(str(x))
    if shift > length:
        shift = shift % length
    shift = -shift
    n = 0
    l = []
    while x / 10:
        q = x // 10
        l.append((x % 10) + n)
        x = q
        n = 0
    l.append((x % 10) + n)
    for i in range(length):
        l[i] += shift
        if l[i] > 9:
            l[i] -= 10
            l[i + 1] += 1
    l.reverse()
    ans = ''
    for i in range(length):
        ans += str(l[i])
    return ans

