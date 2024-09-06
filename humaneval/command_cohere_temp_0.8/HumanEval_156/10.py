```python
def int_to_mini_roman(n):
    if n < 1000 and n > 0:
        roman_map = [
            ('i', 'iv', 'vi', 'ix'),
            ('v', 'vi', 'vii', 'viii', 'ix'),
            ('x', 'l', 'lx', 'lxi', 'lxii', 'lxiii'),
            ('xx', 'lxx', 'lxxx', 'lxxxx', 'lxxxi', 'lxxxi', 'lxxxii', 'lxxxiii'),
            ('xxx', 'lxxx', 'lxxxx', 'lxxxxx', 'lxxxxi', 'lxxxxi', 'lxxxxii', 'lxxxxiii', 'lxxxxiv', 'lxxxxvi', 'lxxxxvii', 'lxxxxviii', 'lxxxxix'),
            ('xxxx', 'xxxxx', 'xxxxxx', 'xxxxxxx', 'xxxxxi', 'xxxxxi', 'xxxxxxxii', 'xxxxxxxiii', 'xxxxxxxiv', 'xxxxxxxvi', 'xxxxxxxvii', 'xxxxxxxviii', 'xxxxxxxix', 'xxxxxl'),
            ('xxxxx', 'xxxxxx', 'xxxxxxx', 'xxxxxxxx', 'xxxxxli', 'xxxxxli', 'xxxxxxxxii', 'xxxxxxxxiii', 'xxxxxxxxiv', 'xxxxxxxxvi', 'xxxxxxxxvii', 'xxxxxxxxviii', 'xxxxxxxxix', 'xxxxxlix'),
            ('xxxxxx', 'xxxxxxx', 'xxxxxxxx', 'xxxxxxxxx', 'xxxxxxli', 'xxxxxxli', 'xxxxxxxxxi', 'xxxxxxxxxi', 'xxxxxxxxxxx', 'xxxxxxxxxxx', 'xxxxxxxxxli', 'xxxxxxxxxli', 'xxxxxxxxxxx', 'xxxxxxxxxxx'),
            ('xxxxxxx', 'xxxxxxxx', 'xxxxxxxxx', 'xxxxxxxxxx', 'xxxxxxxli', 'xxxxxxxli', 'xxxxxxxxxxi', 'xxxxxxxxxxi', 'xxxxxxxxxxx', 'xxxxxxxxxxx', 'xxxxxxxxxxx', 'xxxxxxxxxli', 'xxxxxxxxxli', 'xxxxxxxxxxx', 'xxxxxxxxxxx'),
            ('xxxxxxxx', 'xxxxxxxxx', 'xxxxxxxxxx', 'xxxxxxxxxxx', 'xxxxxxxxli', 'xxxxxxxxli', 'xxxxxxxxxxx', 'xxxxxxxxxxx', 'xxxxxxxxxxx', 'xxxxxxxxxli', 'xxxxxxxxxli', 'xxxxxxxxxxx', 'xxxxxxxxxxx', 'xxxxxxxxxli', 'xxxxxxxxxli'),
            ('xxxxxxxxx', 'xxxxxxxxxx', 'xxxxxxxxxxx', 'xxxxxxxxxxxx', 'xxxxxxxxxli', 'xxxxxxxxxli', 'xxxxxxxxxxx', 'xxxxxxxxxxx', 'xxxxxxxxxli', 'xxxxxxxxxli', 'xxxxxxxxxli', 'xxxxxxxxxli', 'xxxxxxxxxxx', 'xxxxxxxxxxx', 'xxxxxxxxxli'),
            ('xxxxxxxxxx', 'xxxxxxxxxxx', 'xxxxxxxxxxxx', 'xxxxxxxxxxxxx', 'xxxxxxxxxlii', 'xxxxxxxxxlii', 'xxxxxxxxxxx', 'xxxxxxxxxxx', 'xxxxxxxxxlii', 'xxxxxxxxxlii', 'xxxxxxxxxlii', 'xxxxxxxxxlii', 'xxxxxxxxxli', 'xxxxxxxxxli', 'xxxxxxxxxlii'),
            ('xxxxxxxxxxx', 'xxxxxxxxxxxx', 'xxxxxxxxxxxxx', 'xxxxxxxxxxxxxx', 'xxxxxxxxxliii', 'xxxxxxxxxliii', 'xxxxxxxxxli', 'xxxxxxxx