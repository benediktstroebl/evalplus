```python
def int_to_mini_roman(n):
    if n < 1000 and n > 0:
        roman_numbers = [
            'i', 'ii', 'iii', 'iv', 'v', 'vi', 'vii', 'viii', 'ix', 'x', 'xi', 'xii',
            'xiii', 'xiv', 'xv', 'xvi', 'xvii', 'xviii', 'xix', 'xx', 'xxi', 'xxii',
            'xxiii', 'xxiv', 'xxv', 'xxvi', 'xxvii', 'xxviii', 'xxix', 'xxx', 'xlii', 'xliii',
            'xliv', 'xlv', 'xlvi', 'xlvii', 'xlviii', 'xlix', 'l', 'li', 'lii', 'liii', 'liv',
            'lv', 'lvi', 'lvii', 'lviii', 'lix', 'lx', 'lxi', 'lxii', 'lxiii', 'lxiv', 'lxv',
            'lxvi', 'lxvii', 'lxviii', 'lxix', 'lxx', 'lxxi', 'lxxii', 'lxxiii', 'lxxiv', 'lxxv',
            'lxxvi', 'lxxvii', 'lxxviii', 'lxxix', 'lxxx', 'xc', 'xi', 'xii', 'xiii', 'xiv',
            'xv', 'xvi', 'xvii', 'xviii', 'xix', 'xx', 'xxi', 'xxii', 'xxiii', 'xxiv', 'xxv',
            'xxvi', 'xxvii', 'xxviii', 'xxix', 'xxx', 'xli', 'xlii', 'xliii', 'xliv', 'xlv',
            'xlvi', 'xlvii', 'xlviii', 'xlix', 'l', 'li', 'lii', 'liii', 'liv', 'lv', 'lvi',
            'lvii', 'lviii', 'lix', 'lx', 'lxi', 'lxii', 'lxiii', 'lxiv', 'lxv', 'lxvi',
            'lxvii', 'lxviii', 'lxix', 'lxx', 'lxxi', 'lxxii', 'lxxiii', 'lxxiv', 'lxxv',
            'lxxvi', 'lxxvii', 'lxxviii', 'lxxix', 'lxxx', 'xc', 'xi', 'xii', 'xiii', 'xiv',
            'xv', 'xvi', 'xvii', 'xviii', 'xix', 'xx', 'xxi', 'xxii', 'xxiii', 'xxiv', 'xxv',
            'xxvi', 'xxvii', 'xxviii', 'xxix', 'xxx', 'xli', 'xlii', 'xliii', 'xliv', 'xlv',
            'xlvi', 'xlvii', 'xlviii', 'xlix', 'l', 'li', 'lii', 'liii', 'liv', 'lv', 'lvi',
            'lvii', 'lviii', 'lix', 'lx', 'lxi', 'lxii', 'lxiii', 'lxiv', 'lxv', 'lxvi',
            'lxvii', 'lx