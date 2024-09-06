def int_to_mini_roman(n):
    if n < 1:
        raise ValueError("Input must be a positive integer")
    if n < 61:
        return list(str(n))
    elif n < 91:
        return [str(n)[-2]] + ['i', 'ii', 'iii', 'iv', 'v']
    elif n < 121:
        return [str(n)[-2]] + ['vi', 'vii', 'viii', 'ix', 'x']
    elif n < 181:
        return [str(n)[-2]] + ['xi', 'xii', 'xiii', 'xiv', 'xv']
    elif n < 201:
        return [str(n)[-2]] + ['xvi', 'xvii', 'xviii', 'xix', 'xx']
    elif n < 221:
        return [str(n)[-2]] + ['xxi', 'xxii', 'xxiii', 'xxiv', 'xxv']
    elif n < 241:
        return [str(n)[-2]] + ['xxvi', 'xxvii', 'xxviii', 'xxix', 'xxx']
    elif n < 261:
        return [str(n)[-2]] + ['xxxi', 'xxxii', 'xxxiii', 'xxxiv', 'xxxv']
    elif n < 281:
        return [str(n)[-2]] + ['xxxvi', 'xxxvii', 'xxxviii', 'xxxix', 'xl']
    elif n < 301:
        return [str(n)[-2]] + ['xli', 'xlii', 'xliii', 'xliv', 'xlv']
    elif n < 321:
        return [str(n)[-2]] + ['xlvi', 'xlvii', 'xlviii', 'xlix', 'l']
    elif n < 361:
        return [str(n)[-2]] + ['li', 'lii', 'liii', 'liv', 'lv']
    elif n < 381:
        return [str(n)[-2]] + ['lvi', 'lvii', 'lviii', 'lix', 'lx']
    elif n < 401:
        return [str(n)[-2]] + ['lxi', 'lxii', 'lxiii', 'lxiv', 'lxv']
    elif n < 421:
        return [str(n)[-2]] + ['lxvi', 'lxvii', 'lxviii', 'lxix', 'lxx']
    elif n < 441:
        return [str(n)[-2]] + ['lxxi', 'lxxii', 'lxxiii', 'lxxiv', 'lxxv']
    elif n < 461:
        return [str(n)[-2]] + ['lxxvi', 'lxxvii', 'lxxviii', 'lxxix', 'lxxx']
    elif n < 481:
        return [str(n)[-2]] + ['lxxxi', 'lxxxii', 'lxxxiii', 'lxxxiv', 'lxxxv']
    elif n < 501:
        return [str(n)[-2]] + ['lxxxvi', 'lxxxvii', 'lxxxviii', 'lxxxix', 'xc']
    elif n < 521:
        return [str(n)[-2]] + ['xci', 'xcii', 'xciii', 'xciv', 'xcv']