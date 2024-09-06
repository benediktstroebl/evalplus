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
        return "Error!"

roman = {'i': 'i', 'v': 'v', 'x': 'x', 'l': 'l', 'c': 'c', 'd': 'cd', 'm': 'cm', 'xiii': 'xiii', 'xv': 'xv', 'xix': 'xix', 'xxii': 'xxii', 'xxv': 'xxv', 'xxx': 'xxx', 'lxx': 'lxx', 'lxxx': 'lxxx', 'xc': 'xc', 'xcix': 'xcix', 'xcii': 'xcii', 'xciii': 'xciii', 'xciv': 'xciv', 'xcv': 'xcv', 'xcvi': 'xcvi', 'xcvii': 'xcvii', 'xcviii': 'xcviii', 'xcix': 'xcix', 'xi': 'xi', 'xii': 'xii', 'xiii': 'xiii', 'xiv': 'xiv', 'xv': 'xv', 'xvi': 'xvi', 'xvii': 'xvii', 'xviii': 'xviii', 'xix': 'xix', 'xx': 'xx', 'xxi': 'xxi', 'xxii': 'xxii', 'xxiii': 'xxiii', 'xxiv': 'xxiv', 'xxv': 'xxv', 'xxvi': 'xxvi', 'xxvii': 'xxvii', 'xxviii': 'xxviii', 'xxix': 'xxix', 'xxx': 'xxx', 'xxxi': 'xxxi', 'xxxii': 'xxxii', 'xxxiii': 'xxxiii', 'xxxiv': 'xxxiv', 'xxxv': 'xxxv', 'xxxvi': 'xxxvi', 'xxxvii': 'xxxvii', 'xxxviii': 'xxxviii', 'xxxix': 'xxxix', 'xxl': 'xxl', 'xxli': 'xxli', 'xli': 'xli', 'xlii': 'xlii', 'xliii': 'xliii', 'xliv': 'xliv', 'xlv': 'xlv', 'xlvi': 'xlvi', 'xlvii': 'xlvii', 'xlviii': 'xlviii', 'xlix': 'xlix', 'l': 'l', 'li': 'li', 'lvi': 'lvi', 'lvii': 'lvii', 'lviii': 'lviii', 'lix': 'lix', 'lx': 'lx', 'lxi': 'lxi', 'lxii': 'lxii', 'lxiii': 'lxiii', 'lxiv': 'lxiv', 'lxv': 'lxv', 'lxvi': 'lxvi', 'lxvii': 'lxvii', 'lxviii': 'lxviii', 'lxix': 'lxix', 'lxx': 'lxx', 'lxxi': 'lxxi', 'lxxii': 'lxxii', 'lxxiii': 'lxxiii', 'lxxiv': 'lxxiv', 'lxxv':