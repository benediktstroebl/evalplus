def starts_one_ends(n):
    """
    Given a positive integer n, return the count of the numbers of n-digit positive integers that start or end with 1.
    """
    # Define the list of digits from 0 to N-1, where N is the base representing the n-th power of 10.
    base = 10**(n - 1)
    # Generate all the numbers from 0 to N-1 in a list.
    digits = list(range(base))
    # Define the starting and ending digits to be 1.
    start = 1
    end = 1
    # Initialize the count of numbers with 1 as start or end.
    count = 0
    # Iterate through the list of digits, shifting the starting digit to the end and the ending digit to the start.
    for i in range(n):
        digits[i], digits[n - 1 - i] = digits[n - 1 - i], digits[i]
        # Update the start and end if the number is a permutation of digits.
        if tuple(digits) == tuple(str(base // 10**i) for i in range(n)):
            if (start == 1 or end == 1) and base != 1:
                count += 1
            start = end
            end = 1
            base //= 10
    return count