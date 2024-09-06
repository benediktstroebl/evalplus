def eat(n, need, rem):
    ate = n
    if ate + need > rem:
        (ate) = rem
    print(f"You the rabbit, have eaten {ate} carrots and still have {rem-ate} carrots left to eat!")
    return [ate, rem-ate]