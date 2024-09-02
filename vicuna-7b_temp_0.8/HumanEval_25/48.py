from typing import List


def factorize(n: int) -> List[int]:
    """ Return list of prime factors of given integer in the order from smallest to largest.
    Each of the factors should be listed number of times corresponding to how many times it appeares in factorization.
    Input number should be equal to the product of all factors
    >>> factorize(8)
    [2, 2, 2]
    >>> factorize(25)
    [5, 5]
    >>> factorize(70)
    [2, 5, 7]
    """
    # We will use a stack to keep track of factors
    stack = []
    # We will use a queue to keep track of what we have to multiply
    queue = []
    # We will use a dictionary to store the number of times each factor appears
    freq = {}
    # We will use a variable to store the current factor
    current_factor = 1
    # We will use a variable to store the current number
    current_number = n

    while current_number != 1:
        # We will pop the last element from the queue
        # We will multiply it with the current factor
        # We will push the product back to the queue
        # We will increment the current factor
        product = queue[-1]
        product *= current_factor
        queue.append(product)
        current_factor += 1

        # If we have reached the base case
        if current_factor == current_number:
            # We will push the current factor to the stack
            stack.append(current_factor)

            # We will pop the last element from the stack
            current_factor = freq[current_factor]

            # We will multiply it with the current number
            product = current_factor * current_number

            # We will push the product to the queue
            queue.append(product)

    # We will return the list of factors
    return stack
