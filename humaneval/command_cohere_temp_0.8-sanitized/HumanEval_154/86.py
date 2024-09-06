def cycpattern_check(first, second):
    return second in rotated_words(first)
def rotated_words(word):
    return ['', word[i:]] + ([word[i:] + word[:i]] for i in range(1, len(word)))