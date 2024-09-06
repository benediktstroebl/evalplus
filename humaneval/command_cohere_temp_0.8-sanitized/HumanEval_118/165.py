def get_closest_vowel(word):
    vowels = 'AEIOUaeiou'
    ll, rr = 0, len(word) - 1
    for l, r in zip(word, word[1:]):
        if l in vowels and r in vowels:
            if (ll == rr) or (l != r):
                return l
        elif l in consonants and r in consonants:
            ll = rr = l
        elif l in vowels or r in vowels:
            ll, rr = l, r
    return ''
def consonants():
    return 'bcdfghjklmnpqrstvwxyzBCDFGHJKLMNPQRSTVWXYZ'