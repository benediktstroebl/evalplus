def eat(n, need, rem):
    delta = need - n
    result = [n + delta, min(delta, rem)]
    return result if result[1] > 0 else [result[0], 0]