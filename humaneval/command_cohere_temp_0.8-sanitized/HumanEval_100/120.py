def make_a_pile(n):
    if n == 0:
        return []
    pile = [n]
    while len(pile) < n + 1:
        if len(pile) % 2 == 1:
            pile.append(pile[-1] + 2)
        else:
            pile.append(pile[-1] + 1)
    return pile