def int_to_mini_roman(n):
    if n < 1:
        return ""
    
    mini_roman = []
    
    for i in range(1, 1000):
        if n >= i:
            mini_roman.extend(str(i))
            n -= i
    
    mini_roman = ''.join(mini_roman)
    return mini_roman.lower()