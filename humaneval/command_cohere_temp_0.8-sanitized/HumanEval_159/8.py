def eat(n, need, remaining):
    # Plan:
    # 1. Calculate the total number of carrots eaten (n + need).
    # 2. Subtract this from the total remaining carrots to determine the final remaining amount.
    # 3. Return the counts of eaten carrots and the final remaining carrots.
    total_ate, total_left = n + need, remaining
    if total_left >= total_ate:
        return [total_ate, total_left - total_ate]
    else:
        return [remaining, 0]