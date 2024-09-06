
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
    # Your code here.

    even_odd = ['even', 'odd']
    odd = 1
    even = 2
    # creates a list containing all the odd numbers from 1 to n
    odds = [odd] * n
    # creates a list containing all the even numbers from 2 to n
    evens = [even] * n
    # switches between the even and odd lists every other number
    list = []
    for i in range(2 * n - 1):
        if i % 2 == 0:
            list.append(evens)
        else:
            list.append(odds)
    # flattens the list of lists into one list
    flat_list = [num for sublist in list for num in sublist]
    # creates a list containing the total number of stones per level
    stone_count = [sum(flat_list[i:i + 2]) for i in range(0, len(flat_list), 2)]
    return stone_count

