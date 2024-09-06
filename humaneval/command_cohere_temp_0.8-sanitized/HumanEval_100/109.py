def make_a_pile(n):
    # Base case: for n=1, the pile is completed
    if n == 1:
        return [1]
    # For odd n, add 2 and remove 1 to find next valid level
    # e.g.: 3 => 5 => 7 => 9
    pile = [n]
    while len(pile) < n:
        if len(pile) % 2 == 1:
            pile.append(pile[-1] + 2 - 1)
        else:
            pile.append(pile[-1] + 2)
    return pile