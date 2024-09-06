def is_happy(s):
    if len(s) < 3:
        return False
    letters_dict = {}
    letters_list = []
    for i in range(len(s)-2):
        letters_list.append(s[i:i+3])
    for l in letters_list:
        if l not in letters_dict:
            letters_dict[l] = 1
        else:
            letters_dict[l] += 1
    for i in letters_dict:
        if letters_dict[i] == 2:
            return False
    return True