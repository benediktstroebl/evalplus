def eat(n, need, rem):
    eat_all = min(n + need, rem)
    full, hungry = divmod(eat_all, n + need)
    return [full, hungry] if hungry else [full, 0]