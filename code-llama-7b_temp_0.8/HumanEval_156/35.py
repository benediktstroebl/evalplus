
def int_to_mini_roman(number):
    """
    Given a positive integer, obtain its roman numeral equivalent as a string,
    and return it in lowercase.
    Restrictions: 1 <= num <= 1000

    Examples:
    >>> int_to_mini_roman(19) == 'xix'
    >>> int_to_mini_roman(152) == 'clii'
    >>> int_to_mini_roman(426) == 'cdxxvi'
    """
    # incremental values for 10s
    M, C, X, I = 1000, 100, 10, 1
    # list of tuples of (incremental value, character, 10s counter)
    tups = [(M, 'm', 0), (C, 'c', 1), (X, 'x', 2), (I, 'i', 3)]
    # roman numerals are built in reverse, starting with the biggest digit
    # we'll be building a list of roman numeral characters
    chars = []
    # make sure the number is positive
    num = abs(number)
    # loop through our tuples, 3 times (10s, 10s, 10s)
    for tup in tups * 3:
        # is the number greater than the incremental value?
        if num >= tup[0]:
            # number of times to append the character
            char_count = num // tup[0]
            # append the character
            chars.append(tup[1] * char_count)
            # subtract the incremental value * number of times
            num -= tup[0] * char_count
            # if we're at a 10s, increment the counter
            if tup[2] > 0:
                # increment the counter
                tup[2] += 1
    # join the characters together
    return ''.join(chars)

