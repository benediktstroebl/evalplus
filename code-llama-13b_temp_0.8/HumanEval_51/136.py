

def remove_vowels(text):
    """
    remove_vowels is a function that takes string and returns string without vowels.
    >>> remove_vowels('')
    ''
    >>> remove_vowels("abcdef\nghijklm")
    'bcdf\nghjklm'
    >>> remove_vowels('abcdef')
    'bcdf'
    >>> remove_vowels('aaaaa')
    ''
    >>> remove_vowels('aaBAA')
    'B'
    >>> remove_vowels('zbcd')
    'zbcd'
    """
    vowels = "aeiou"
    if len(text) == 0:
        return text

    # your code here
    #without using regular expression
    lst = []
    for i in text:
        if i.lower() not in vowels:
            lst.append(i)
    return "".join(lst)
    # using regular expression
    # return re.sub(r"[aeiouAEIOU]", "", text)

