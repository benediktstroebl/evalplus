```python
def int_to_mini_roman(n):
    if n < 1:
        raise ValueError("Input must be a positive integer")

    # Translation mapping where key is integer and value is roman numeral
    translation = {
        1: 'i', 
        2: 'ii', 
        3: 'iii', 
        4: 'iv', 
        5: 'v', 
        6: 'vi', 
        7: 'vii', 
        8: 'viii', 
        9: 'ix', 
        10: 'x',
        11: 'xi',
        12: 'xii',
        13: 'xiii',
        14: 'xiv',
        15: 'xv',
        16: 'xvi',
        17: 'xvii',
        18: 'xviii',
        19: 'xix',
        20: 'xx',
        21: 'xxi',
        22: 'xxii',
        23: 'xxiii',
        24: 'xxiv',
        25: 'xxv',
        26: 'xxvi',
        27: 'xxvii',
        28: 'xxviii',
        29: 'xxix',
        30: 'xxx'
    }

    result = []
    for k, v in translation.items():
        while n >= k:
            result.append(v)
            n -= k

    return ''.join(result)
```

This script provides a function `int_to_mini_roman` that takes a positive integer as input and returns its roman numeral equivalent as a string in lowercase. It utilizes a translation mapping to perform the conversion. This code handles boundaries and constraints as specified in the problem statement.