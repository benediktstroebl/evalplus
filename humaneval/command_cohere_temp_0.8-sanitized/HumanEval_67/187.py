def fruit_distribution(s,n):
    apples, oranges = map(int, s.split(' and '))
    if n < apples + oranges:
        return "Error: Basket is empty!"
    return n - apples - oranges