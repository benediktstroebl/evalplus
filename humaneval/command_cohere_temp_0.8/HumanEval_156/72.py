```python
def int_to_mini_roman(n):
    if n < 1000:
        res = []
        for x in range(0, n + 1):
            if x != 0:
                res.append(mini_roman[x])
        res.reverse()
        return ''.join(res)
    else:
        return 'Error: Restrictions are 1 <= num <= 1000'

mini_roman = [
    'i', 'ii', 'iii', 'iv', 'v', 'vi', 'vii', 'viii', 'ix', 'x',
    'xi', 'xii', 'xiii', 'xiv', 'xv', 'xvi', 'xvii', 'xviii', 'xix',
    'xx', 'xxi', 'xxii', 'xxiii', 'xxiv', 'xxv', 'xxvi', 'xxvii', 'xxviii', 'xxix',
    'xxx', 'xxxi', 'xxxii', 'xxxiii', 'xxxiv', 'xxxv', 'xxxvi', 'xxxvii', 'xxxviii', 'xxxix',
    'xl', 'xli', 'xlii', 'xliii', 'xliv', 'xlv', 'xlvi', 'xlvii', 'xlviii', 'xlix',
    'l', 'li', 'lii', 'liii', 'liv', 'lv', 'lvi', 'lvii', 'lviii', 'lix',
    'lx', 'lxi', 'lxii', 'lxiii', 'lxiv', 'lxv', 'lxvi', 'lxvii', 'lxviii', 'lxix',
    'lxx', 'lxxi', 'lxxii', 'lxxiii', 'lxxiv', 'lxxv', 'lxxvi', 'lxxvii', 'lxxviii', 'lxxix',
    'lxxx', 'lxxxi', 'lxxxii', 'lxxxiii', 'lxxxiv', 'lxxxv', 'lxxxvi', 'lxxxvii', 'lxxxviii', 'lxxxix',
    'xc', 'xci', 'xcii', 'xciii', 'xciv', 'xcv', 'xcvi', 'xcvii', 'xcviii', 'xcix',
    'c', 'ci', 'cii', 'ciii', 'civ', 'cv', 'cvi', 'cvii', 'cviii', 'cix',
    'cx', 'cxi', 'cxii', 'cxiii', 'cxiv', 'cxv', 'cxvi', 'cxvii', 'cxviii', 'cxix',
    'cxx', 'cxxi', 'cxxii', 'cxxiii', 'cxxiv', 'cxxv', 'cxxvi', 'cxxvii', 'cxxviii', 'cxxix',
    'cxxx', 'cxxxi', 'cxxxii', 'cxxxiii', 'cxxxiv', 'cxxxv', 'cxxxvi', 'cxxxvii', 'cxxxviii', 'cxxxix',
    'xd', 'xi', 'xdii', 'xdiii', 'xdiv', 'xdv', 'xdvi', 'xdvii', 'xdviii', 'xdix',
    'd', 'di', 'dii', 'diii', 'div', 'dv', 'dvi', 'dvii', 'dv