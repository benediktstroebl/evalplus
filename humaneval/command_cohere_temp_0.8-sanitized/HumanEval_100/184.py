def make_a_pile(n):
    # Base case: if n is 0, return a list with a single 0
    if n == 0:
        return [0]
    
    # Initial list with n amount of stones
    pile = [n]
    
    # odd and even bases for the next levels
    odd, even = n % 2, n // 2
    
    # Loop for the next levels
    for _ in range(1, n // 2 + 1):
        # if the level is odd, add the next odd number of stones
        if _ % 2 == 1:
            pile.append(odd)
            odd += 2
        # if the level is even, add the next even number of stones
        else:
            pile.append(even)
            even += 2
    
    return pile