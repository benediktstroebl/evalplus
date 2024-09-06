def eat(n, need, rem):
    # eat all needed carrots
    n, rem = n + need, rem - need
    
    # check if there are enough carrots, and adjust n and rem accordingly
    if rem < need:
        n, rem = n + (need - rem), 0
    
    return [n, rem]