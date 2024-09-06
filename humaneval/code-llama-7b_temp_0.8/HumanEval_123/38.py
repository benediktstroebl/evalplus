
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
    # Initialize variables
    list_of_odd = []
    number = n
    # Loop through the numbers in the list until the current number is 1
    while number != 1:
        if number % 2 != 0:
            list_of_odd.append(number)
            number = number * 3 + 1
        elif number % 2 == 0:
            number = number / 2
    # Add 1 to the list as the conjecture is that it will reach 1
    list_of_odd.append(1)
    # Return the list in sorted order
    return sorted(list_of_odd)

