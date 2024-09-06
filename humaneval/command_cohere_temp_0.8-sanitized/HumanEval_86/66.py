def anti_shuffle(s):
    word_arr = []
    word_flag = False 
    ascii_flag = False

    for char in s:
        if char == " ":
            if word_flag:
                word_arr.append(char)
            else:
                ascii_flag = True
        elif char.isalpha():
            if ascii_flag:
                temp = ''.join(sorted(char))
                word_arr.append(temp)
                ascii_flag = False
            else:
                word_flag = True
        else:
            word_arr.append(char)

    return ' '.join(word_arr)