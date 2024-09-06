def file_name_check(file_name):
    digits = ''.join('0123456789')
    dot = '.'
    latin_alphabet = ''.join('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ' )
    valid_ext = ['txt', 'exe', 'dll']

    if len(file_name) == 0:
        return "No"

    file_name = file_name.lower()
    num_digits = sum(1 for c in file_name if c in digits)
    
    if num_digits > 3:
        return "No"
    elif num_digits == 0:
        pos = file_name.find(dot)
        if pos == -1:
            return "No"
        pre_dot = file_name[:pos]
        if not (pre_dot[0] in latin_alphabet and pre_dot[0] != ""):
            return "No"
        post_dot = file_name[pos+1:]
        if post_dot not in valid_ext:
            return "No"
    return "Yes"