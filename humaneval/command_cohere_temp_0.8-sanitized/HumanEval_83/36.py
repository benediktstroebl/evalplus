def starts_one_ends(n):
    pos_ints = [str(i) for i in range(1, n + 1)]
    # Setting up the counting variables.
    starts_one = ends_one = 0
    for int in pos_ints:
        if int[0] == '1' or int[-1] == '1':
            starts_one += 1
        if int[0] == '1' or int[-1] == '1':
            ends_one += 1
    return starts_one + ends_one