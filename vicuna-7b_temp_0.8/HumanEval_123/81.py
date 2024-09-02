
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
    # Check if n is odd or even
    if n % 2 == 0:
        n = n + (n // 2)
    # Initialize a list to store the sorted odd numbers
    list_of_odd_numbers = []
    # Starting with n, we iterate through the odd numbers
    for i in range(1, n + 1):
        # If the current number is already in the list, add it to the front
        if i not in list_of_odd_numbers:
            list_of_odd_numbers.append(i)
        # Otherwise, check if it is even, and if so, add the odd number to the
        # front of the list and the even number to the end of the list
        else:
            list_of_odd_numbers[list_of_odd_numbers.index(i)] = i % 2 != 0
    # Sort the list in ascending order
    list_of_odd_numbers = sorted(list_of_odd_numbers)
    # Return the sorted list
    return list_of_odd_numbers
