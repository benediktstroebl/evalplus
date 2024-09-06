def eat(n, need, remaining):
    # plan your meal
    result = n + need
    if result > remaining:
        result = remaining
    hungry = True
    if result >= need:
        # lunch completed, you're full
        hungry = False
        result = need
    return [result, remaining - result]