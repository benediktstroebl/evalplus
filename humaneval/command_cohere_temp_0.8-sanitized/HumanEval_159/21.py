def eat(n, need, rem):
    val = n + need
    if val > rem:
        val = rem
    return [val, rem-val]