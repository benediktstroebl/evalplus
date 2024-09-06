def make_a_pile(n):
    # Calculate the pile size
    pile_size = [n]
    while len(pile_size) < n:
        if len(pile_size) % 2 == 0:
            pile_size.append(pile_size[-1] + 2)
        else:
            pile_size.append(pile_size[-1] + 1)
    return pile_size