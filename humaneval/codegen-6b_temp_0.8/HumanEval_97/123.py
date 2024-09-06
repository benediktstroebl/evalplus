
def multiply(a, b):
    """Complete the function that takes two integers and returns 
    the product of their unit digits.
    Assume the input is always valid.
    Examples:
    multiply(148, 412) should return 16.
    multiply(19, 28) should return 72.
    multiply(2020, 1851) should return 0.
    multiply(14,-15) should return 20.
    """
    lt = len(a)
    lb = len(b)
    sa = [int(x) for x in str(a)]
    sb = [int(x) for x in str(b)]

    # calcuat the sum of the digits of each string
    sa_sum = 0
    for x in sa:
        sa_sum += x

    sb_sum = 0
    for x in sb:
        sb_sum += x

    # make sure the length of a is longer than b
    if sa_sum >= sb_sum:
        diff = sa_sum - sb_sum
        for x in range(diff):
            sa.append(0)

    else:
        diff = sb_sum - sa_sum
        for x in range(diff):
            sb.append(0)
    
    # make sure the two strings are the same length
    sa_len = len(sa)
    sb_len = len(sb)
    if sa_len != len(sb):
        if sa_len > sb_len:
            diff = sa_len - sb_len
            for x in range (diff):
                sb.append(0)
        elif sb_len > sa_len:
            diff = sb_len - sa_len
            for x in range (diff):
                sa.append(0)

    # multiply the two strings
    result = [0] * sa_len

    for i in range(sa_len):
        result[sa_len - i - 1] = (sa[i] * sb[i])

    return result
