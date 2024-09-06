def eat(n, need, rem):
    ate = n
    if need > rem:
        ate = rem
    self_hungry = need - ate
    return [ate, self_hungry]