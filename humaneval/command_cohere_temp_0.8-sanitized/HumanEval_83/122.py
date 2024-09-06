def starts_one_ends(n):
    pos_ints = [str(i) for i in range(1, n + 1)]
    pos_ints_starting_with_1 = [i for i in pos_ints if i[0] == '1']
    pos_ints_ending_with_1 = [i for i in pos_ints if i[-1] == '1']
    
    return len(pos_ints_starting_with_1) + len(pos_ints_ending_with_1)