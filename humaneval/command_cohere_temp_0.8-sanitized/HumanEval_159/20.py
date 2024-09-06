def eat(n, need, rem):
    eatsome = min(need, rem)
    n += eatsome
    rem -= eatsome
    return [n, rem]