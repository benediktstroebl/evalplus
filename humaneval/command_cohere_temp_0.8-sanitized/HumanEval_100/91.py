def make_a_pile(n):
    # Generate the sequence of stone counts based on the given rules.
    # Since the problem states that the first level has n stones, the sequence starts with n.
    sequence = [n]
    
    # If the level number is even, the stone count should be the next even number.
    # If the level number is odd, the stone count should be the next odd number.
    # Increment the stone count by 2*((level_number + 1) % 2) + 1 to achieve this.
    for level_number in range(1, n + 1):
        sequence.append(2 * ((level_number + 1) % 2) + 1)

    return sequence