
def make_a_pile(n):
    """
    Given a positive integer n, you have to make a pile of n levels of stones.
    The first level has n stones.
    The number of stones in the next level is:
        - the next odd number if n is odd.
        - the next even number if n is even.
    Return the number of stones in each level in a list, where element at index
    i represents the number of stones in the level (i+1).

    Examples:
    >>> make_a_pile(3)
    [3, 5, 7]
    """
    # The number of stones in the next level is determined by the parity of n
    odd_next_number = [n + 1 if n % 2 == 0 else n + 2 for n in range(1, len(inputs))]
    even_next_number = [n + 2 if n % 2 == 0 else n + 1 for n in range(1, len(inputs))]
    
    return [inputs[i] + odd_next_number[i] for i in range(1, len(inputs))]

inputs = list(map(int, input().split()))
result = make_a_pile(inputs[0])
