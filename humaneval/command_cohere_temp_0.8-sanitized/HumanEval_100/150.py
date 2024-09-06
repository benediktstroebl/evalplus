def make_a_pile(n):
    pile = [n]
    while len(pile) < n + 1:
        if n % 2 == 1:
            n += 2
        else:
            n = n + 1 if n == 0 else n + 3
        pile.append(n)
    return pile