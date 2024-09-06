def make_a_pile(n):
    if n == 0:
        return []
    pile = [n]
    while len(pile) < n + 1:
        if len(pile) % 2 == 1 and pile[-1] % 2 == 0:
            pile.append(pile[-1] + 1)
        elif len(pile) % 2 == 0 and pile[-1] % 2 == 1:
            pile.append(pile[-1] - 1)
        else:
            pile.append(pile[-1])
    return pile