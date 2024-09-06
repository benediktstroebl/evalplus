def eat(n, need, rem):
    ct, leftovers = 0, n
    while need > 0:
        if leftovers == 0:
            return [ct, leftovers]
        ct += 1
        need -= 1
        leftovers -= 1
    return [ct, leftovers]