def file_name_check(file_name):
    lat_alphabet = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
    num_dot = 0
    act_sub = file_name.split('.')

    if len(act_sub[0]) == 0 or (act_sub[0][0] not in lat_alphabet):
        return "No"
    else:
        if len(act_sub[0]) > 3: 
            return "No"
        
        if file_name.endswith('.txt') or file_name.endswith('.exe') or file_name.endswith('.dll'):
            return "Yes"
        else:
            return "No"