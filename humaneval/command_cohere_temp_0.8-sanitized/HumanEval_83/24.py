def starts_one_ends(n):
    pos_num = str(n)
    if pos_num.isdigit():
        num_list = [int(val) for val in pos_num]
        if num_list[0] == 1 or num_list[-1] == 1:
            return 2
        else:
            return 1
    else:
        return 0