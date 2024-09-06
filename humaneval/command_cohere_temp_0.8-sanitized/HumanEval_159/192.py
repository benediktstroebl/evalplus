def eat(n, need, rem):
    cath_meal = min(n + need, rem)
    full = n + cath_meal
    return [full, rem - cath_meal]