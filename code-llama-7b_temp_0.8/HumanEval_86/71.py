
def anti_shuffle(s):
    """
    Write a function that takes a string and returns an ordered version of it.
    Ordered version of string, is a string where all words (separated by space)
    are replaced by a new word where all the characters arranged in
    ascending order based on ascii value.
    Note: You should keep the order of words and blank spaces in the sentence.

    For example:
    anti_shuffle('Hi') returns 'Hi'
    anti_shuffle('hello') returns 'ehllo'
    anti_shuffle('Hello World!!!') returns 'Hello !!!Wdlor'
    """
    if len(s) == 0:
        return s
    words = s.split(" ")
    new_words = []
    for word in words:
        new_word = ""
        for char in word:
            if new_word:
                if char < new_word[-1]:
                    new_word += char
            else:
                new_word += char
        new_words.append(new_word)
    return " ".join(new_words)

