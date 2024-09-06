def eat(n, need, rem):
    ate = n
    if ate + need > rem:
        (ate) = rem
    print(f"You the rabbit starts to be greedy and eat as much as {ate} carrots.")
    return [ate, rem - ate]