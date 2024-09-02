
def generate_integers(a, b):
    """
    Given two positive integers a and b, return the even digits between a
    and b, in ascending order.

    For example:
    generate_integers(2, 8) => [2, 4, 6, 8]
    generate_integers(8, 2) => [2, 4, 6, 8]
    generate_integers(10, 14) => []
    """

    # Your code here

    x = int(a)
    y = int(b)

    if a < b:
        res = []
        for n in range(x, y+1):
            n1 = str(n)
            for m in n1:
                if int(m) % 2 != 0:
                    break
                else:
                    res.append(int(m))
        return sorted(list(set(res)))
    elif a > b:
        res = []
        for n in range(x, y+1):
            n1 = str(n)
            for m in n1:
                if int(m) % 2 == 0:
                    break
                else:
                    res.append(int(m))
        return sorted(list(set(res)))
    else:
        return []

