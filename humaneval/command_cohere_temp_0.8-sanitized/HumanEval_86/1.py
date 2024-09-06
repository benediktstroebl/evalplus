def anti_shuffle(s):
    word_arr = []
    word_flag = False 
    spacing = False
    for c in s:
        if c != " " and not word_flag:
            word_arr.append(c)
        elif c == " " and not spacing:
            spacing = True
        elif c == " " and spacing:
            spacing = False
        elif c != " ":
            word_flag = False
        else:
            word_flag = True
    s = "".join(word_arr)
    s = s.upper()
    s = s.replace(" ", "")
    return s