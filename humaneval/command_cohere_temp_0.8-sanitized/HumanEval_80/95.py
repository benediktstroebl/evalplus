def is_happy(s):
    if len(s) < 3:
        return False
    letters_dict = {}
    letters_list = []
    for letter in s:
        if letter in letters_dict:
            letters_dict[letter] += 1
        else:
            letters_dict[letter] = 1
        letters_list.append(letters_dict[letter])
    return all(x != 2 for x in letters_list)