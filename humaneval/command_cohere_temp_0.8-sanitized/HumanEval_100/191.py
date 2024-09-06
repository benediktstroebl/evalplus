def make_a_pile(n):
    # Base case: When n is 1, it forms the initial level of the pile
    if n == 1:
        return [n]
    
    # Initialize an empty list to hold the numbers of stones for each level
    pile = []
    
    # The first level has n stones
    pile.append(n)
    
    # Iterate through numbers from 2 to n (exclusive) to build subsequent levels
    for num in range(2, n + 1):
        # If the current number is odd, the next level should have the next odd number
        if num % 2 == 1:
            pile.append(num + 1)
        # If the current number is even, the next level should have the next even number
        else:
            pile.append(num + 2)
    
    # Return the pile of stones represented as a list
    return pile