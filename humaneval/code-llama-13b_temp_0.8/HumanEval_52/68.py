

def below_threshold(l: list, t: int):
    """Return True if all numbers in the list l are below threshold t.
    >>> below_threshold([1, 2, 4, 10], 100)
    True
    >>> below_threshold([1, 20, 4, 10], 5)
    False
    """
    # ====================================================================
    #   |                                                              |
    #   |  THIS IS THE START OF THE EXERCISE.                           |
    #   |  CHANGE THE CODE BELOW TO MAKE THE TESTS PASS.                |
    #   |                                                              |
    #   |  You will need to use the 'all' function.                     |
    #   |                                                              |
    # ====================================================================

    return all(i < t for i in l)

    # ====================================================================
    #   |                                                              |
    #   |  IMPLEMENT YOUR SOLUTION BELOW.                               |
    #   |                                                              |
    # ====================================================================

