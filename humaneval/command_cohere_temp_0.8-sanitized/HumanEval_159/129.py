def eat(number, need, remaining):
    total_eaten = number + need
    total_remaining = remaining - need
    return [total_eaten, total_remaining]