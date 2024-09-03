def count_upper(s):
    vowels = 'aeiou'
    return sum(1 for c in s if c in vowels and c.isupper())