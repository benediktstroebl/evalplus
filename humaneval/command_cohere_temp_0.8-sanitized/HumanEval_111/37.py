def histogram(test):
    letters = test.split()
    letters = [letter for letter in letters if letter.isalpha()]
    repeat = {}
    
    for letter in letters:
        if letter in repeat:
            repeat[letter] += 1
        else:
            repeat[letter] = 1
    
    return repeat