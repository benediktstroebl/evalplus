def select_words(s, n):
    consonants = {'b', 'c', 'd', 'f', 'g', 'h', 'j', 'k', 'l', 'm', 'p', 'q', 'r', 's', 't', 'v', 'w', 'x', 'y', 'z'} 
    words = []
    word = ""
    num_consonants = 0
    for c in s:
        if c == ' ':
            if num_consonants == n:
                words.append(word)
            elif num_consonants > n:
                return []
            num_consonants = 0
            word = ""
        elif c in consonants:
            num_consonants += 1
            word += c
    if num_consonants == n:
        words.append(word)
    return words