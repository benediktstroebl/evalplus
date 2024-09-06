def fruit_distribution(s, n):
    "Returns the number of mango fruits in the basket."
    apples, oranges = map(int, s.split(' and '))
    return n - apples - oranges