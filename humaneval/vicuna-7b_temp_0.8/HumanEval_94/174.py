

def skjkasdkd(lst):
    """You are given a list of integers.
    You need to find the largest prime value and return the sum of its digits.

    Examples:
    For lst = [0,3,2,1,3,5,7,4,5,5,5,2,181,32,4,32,3,2,32,324,4,3] the output should be 10
    For lst = [1,0,1,8,2,4597,2,1,3,40,1,2,1,2,4,2,5,1] the output should be 25
    For lst = [1,3,1,32,5107,34,83278,109,163,23,2323,32,30,1,9,3] the output should be 13
    For lst = [0,724,32,71,99,32,6,0,5,91,83,0,5,6] the output should be 11
    For lst = [0,81,12,3,1,21] the output should be 3
    For lst = [0,8,1,2,1,7] the output should be 7
    """
    if not lst:
        return 0
    max_digit = 0
    max_val = 0
    max_digit_lst = lst
    for val in max_digit_lst:
        max_val = max(max_val, int(val))
        max_digit = max(max_digit, int(val))
    max_digit_lst = [str(val)]
    for val in max_digit_lst:
        max_val = max(max_val, int(val))
        max_digit = max(max_digit, int(val))
    max_val_str = str(max_val)
    max_digit_sum = 0
    max_digit_lst_len = len(max_digit_lst)
    for i in range(max_digit_lst_len):
        max_digit_sum = max(max_digit_sum, (max_digit_lst[i].isdigit() and (max_val_str[i] >= '0' and max_val_str[i] <= '9')) and (max_digit_lst[i].isdigit() and (max_val_str[i] >= '0' and max_val_str[i] <= '9')) or (max_digit_lst[i].isdigit() and (max_val_str[i] >= '1' and max_val_str[i] <= '9')) or (max_digit_lst[i].isdigit() and (max_val_str[i] >= '2' and max_val_str[i] <= '9')) or (max_digit_lst[i].isdigit() and (max_val_str[i] >= '3' and max_val_str[i] <= '9')) or (max_digit_lst[i].isdigit() and (max_val_str[i] >= '4' and max_val_str[i] <= '9')) or (max_digit_lst[i].isdigit() and (max_val_str[i] >= '5' and max_val_str[i] <= '9')) or (max_digit_lst[i].isdigit() and (max_val_str[i] >= '6
