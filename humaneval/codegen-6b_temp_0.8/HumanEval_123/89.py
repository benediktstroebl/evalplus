
def get_odd_collatz(n):
    """
    Given a positive integer n, return a sorted list that has the odd numbers in collatz sequence.

    The Collatz conjecture is a conjecture in mathematics that concerns a sequence defined
    as follows: start with any positive integer n. Then each term is obtained from the 
    previous term as follows: if the previous term is even, the next term is one half of 
    the previous term. If the previous term is odd, the next term is 3 times the previous
    term plus 1. The conjecture is that no matter what value of n, the sequence will always reach 1.

    Note: 
        1. Collatz(1) is [1].
        2. returned list sorted in increasing order.

    For example:
    get_odd_collatz(5) returns [1, 5] # The collatz sequence for 5 is [5, 16, 8, 4, 2, 1], so the odd numbers are only 1, and 5.
    """
    # Need to check input is an int
    if type(n) != int: 
        return "Input must be a positive integer"

    # Handle the edge case where n=1
    if n == 1:
        return [1]

    # Initialise list to store collatz sequences
    even_odd_collatz = []

    # Loop through all numbers from 1 to n, starting with 1
    while n > 1:
        # If the previous term is even, append the next term to the list
        if n % 2 == 0:
            even_odd_collatz.append(int(n))
            n = n / 2 # Divide by 2 to get the next term
            # print(n)
        # If the previous term is odd, append the next term to the list
        else:
            even_odd_collatz.append(int(n))
            n = 3 * n + 1 # Multiply by 3 to get the next term
            # print(n)

    # Sort the list in ascending order
    even_odd_collatz.sort()
    return [n for n in even_odd_collatz if n % 2 != 0]


