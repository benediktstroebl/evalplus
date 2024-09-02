
def generate_integers(a, b):
    """
    Given two positive integers a and b, return the even digits between a
    and b, in ascending order.

    For example:
    generate_integers(2, 8) => [2, 4, 6, 8]
    generate_integers(8, 2) => [2, 4, 6, 8]
    generate_integers(10, 14) => []
    """
    # Start with a list of all the odds between a and b, sorted ascendingly.
    integers = [i for i in range(a, b + 1, 2)]

    # If a and b are both even, then just return the list as it is.
    if a % 2 == 0 and b % 2 == 0:
        return integers

    # Otherwise, if a and b are both odd, we need to remove all numbers that
    # aren't between a and b, as they aren't even.
    if a % 2 and b % 2:
        while True:
            if integers[0] % 2 and integers[0] < integers[1]:
                integers.pop(0)
            else:
                break

    # If we have only one number, then we can just remove that number and return
    # it in ascending order.
    if len(integers) == 1:
        return [integers[0]]

    # If we have two numbers, then we can just pop the first number and add it
    # to the second number, which gives us the even number between them.
    elif len(integers) == 2:
        return [integers[0] + integers[1]]

    # If none of the above, we just take the first two numbers, subtract them
    # from each other, add them, and take the new set of numbers.
    else:
        return [integers[0] - integers[1]] + integers[2:]

