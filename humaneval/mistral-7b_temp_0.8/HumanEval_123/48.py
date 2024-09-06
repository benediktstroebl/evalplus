
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
    # TODO: complete this function
    # Initialize a list to store the odd numbers in collatz sequence.
    odd_list = []
    # Initialize a variable to keep track of the current number in the sequence.
    current_number = n
    # Initialize a variable to store the next number in the sequence.
    next_number = None
    # Initialize a flag to keep track of the first odd number in the sequence.
    first_odd_flag = False
    # Initialize a counter to keep track of the length of the sequence.
    sequence_length = 0
    # Loop through the collatz sequence for the current number.
    while True:
        # Compute the next number in the sequence.
        if current_number % 2 == 0:
            next_number = current_number // 2
        else:
            next_number = 3 * current_number + 1
        # Update the current number and the next number in the sequence.
        current_number = next_number
        # Check if the next number is odd.
        if next_number % 2 != 0:
            # If it
