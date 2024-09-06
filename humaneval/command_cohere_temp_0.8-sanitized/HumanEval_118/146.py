def get_closest_vowel(word):
    """
    Finds the closest vowel to the right of a word, assuming the vowels occur between two consonants.
    Ignores starting and ending vowels.
    """
    vowels = 'IEOUaeiou'  
    # Regular expression to match a consonant that is not the last letter
    regex = '[^%s%s]' % (word[0], word[-1])
    
    matches = [m for m in word[1:-1].lower().replace(' ', '').replace('-', '').replace('&', '').split('&') if m in vowels and re.search(regex, m)]
    if matches:
        return matches.pop()
    else:
        return ''