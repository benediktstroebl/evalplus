

def sort_even(l: list):
    """This function takes a list l and returns a list l' such that
    l' is identical to l in the odd indicies, while its values at the even indicies are equal
    to the values of the even indicies of l, but sorted.
    >>> sort_even([1, 2, 3])
    [1, 2, 3]
    >>> sort_even([5, 6, 3, 4])
    [3, 6, 5, 4]
    """

    # Create a list l'
    l_prime = []
    # Create a loop to iterate through every element in l
    for i in range(len(l)):
        # Check if i is even
        if i % 2 == 0:
            # If so, append the value in l at index i to l_prime
            l_prime.append(l[i])
    # Create a loop to iterate through every value in l_prime
    for i in range(len(l_prime)):
        # Check if i is odd
        if i % 2 == 1:
            # If so, append the value in l_prime at index i to l
            l.append(l_prime[i])
    return l

