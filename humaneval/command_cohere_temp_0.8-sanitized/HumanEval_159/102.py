def eat(n, need, rem):
    eat_all = min(n + need, rem)
    full, hungry = divmod(eat_all, n + need)
    return [full * (n + need), hungry * (n + need)]