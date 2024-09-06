def make_a_pile(n):
    # Calculate the first two levels directly
    pile = [n, ]
    if n % 2 == 1:
        pile.append(n + 2)
    else:
        pile.append(n + 1)
    # Use the explicit formula to generate the remaining levels
    for _ in range(len(pile), n):
        pile.append(pile[-1] + 2**(len(pile) - 1))
    return pile