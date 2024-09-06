
def starts_one_ends(n):
    """
    Given a positive integer n, return the count of the numbers of n-digit
    positive integers that start or end with 1.
    """
    # set up a stack from 0-9
    stack = {digit: n for digit in range(10)}
    stack[0] = 0
    stack[1] = 1

    # set up a dict mapping (x, y) to the number of times that (x, y) repeats
    counts = {}
    for i in range(2, n + 1):
        # loop over all numbers in the stack, so that we don't overflow
        for digit in stack.keys():
            if digit == 0:
                continue
            # loop over all possible prefixes and suffixes
            for prefix in stack.keys():
                # we don't want to exceed the length of the stack
                if i > prefix:
                    # start with the prefix
                    if prefix * 10 + digit == i:
                        counts[prefix, digit] = counts.get((prefix, digit), 0) + 1
                    # then the suffix
                    if digit * 10 + prefix == i:
                        counts[digit, prefix] = counts.get((digit, prefix), 0) + 1

    result = 0
    for prefix in counts.keys():
        if prefix[1] in [1, n]:
            result += counts[prefix]

    return result

