def eat(n, need, rem):
    # eating calculation
    eat_all = min(n + need, rem)
    n += eat_all
    rem -= eat_all
    
    # result return
    return [n, rem]