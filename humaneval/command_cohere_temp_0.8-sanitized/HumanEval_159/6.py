def eat(n, need, rem):
    # eat all needed carrots
    n, rem = n + need, rem - need
    
    # handle overshoot and return values
    if n > rem:
        n, rem = rem, 0
    return [n, rem]