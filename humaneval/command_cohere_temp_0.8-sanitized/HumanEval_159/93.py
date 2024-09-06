def eat(n, need, rem):
    ct, leftovers = 0, 0
    while need:
        if rem:
            eat_amount = min(need, rem)
            need -= eat_amount
            rem -= eat_amount
            ct += eat_amount
            leftovers = max(leftovers, eat_amount)
        else:
            break
    return [ct, leftovers]