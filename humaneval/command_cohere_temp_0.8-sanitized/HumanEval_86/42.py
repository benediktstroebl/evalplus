def anti_shuffle(s):
    word_arr = []
    word_flag = False 
    spaced = s.split(' ')
    for word in spaced:
      if word != '':
        word_arr.append(sorted(word))
        word_flag = True
      else:
        if word_flag:
          word_flag = False
          word_arr.append('')
    return (' '.join(map(str, word_arr)))