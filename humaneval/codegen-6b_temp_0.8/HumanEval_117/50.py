
def select_words(s, n):
    """Given a string s and a natural number n, you have been tasked to implement 
    a function that returns a list of all words from string s that contain exactly 
    n consonants, in order these words appear in the string s.
    If the string s is empty then the function should return an empty list.
    Note: you may assume the input string contains only letters and spaces.
    Examples:
    select_words("Mary had a little lamb", 4) ==> ["little"]
    select_words("Mary had a little lamb", 3) ==> ["Mary", "lamb"]
    select_words("simple white space", 2) ==> []
    select_words("Hello world", 4) ==> ["world"]
    select_words("Uncle sam", 3) ==> ["Uncle"]
    """
    if not s:
        return []
    
    word_replacements = {}

    # store first word of each word in replacement dictionary
    for word in s.split():
        word_replacements[word] = word[:n]

    # build replacement dictionary so we know what characters we need to replace
    for word in s.split():
        max_char = n
        for char in word:
            if char in 'aeiou':
                max_char -= 1
                if max_char == 0:
                    break

        # replace all characters with max_char with '*'
        for i in range(len(word)):
            if word[i] in 'aeiou':
                word_replacements[word[:i] + '*' + word[i+1:]] = word[i]

    # replace all characters with '*' with '-'
    for word in word_replacements.keys():
        word_replacements[word.replace('*', '-')] = '-'

    # replace all letters with '-' with '*'
    for word in s.split():
        word_replacements[word.replace('-', '*')] = '-'

    # replace all characters with '-' with '*'
    for word in word_replacements.keys():
        word_replacements[word.replace('*', '-')] = '-'

    return [word_replacements[word] for word in sorted(word_replacements.keys())]

