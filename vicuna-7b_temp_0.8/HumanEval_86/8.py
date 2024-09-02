
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
    words = s.split()
    shuffled_words = []
    current_shuffled_word = ""
    for word in words:
        if len(word) > 0:
            current_shuffled_word += str(ord(word[0]) + len(word)) + word[1:]
        else:
            current_shuffled_word += str(ord(word[0]) + len(word))
        shuffled_words.append(current_shuffled_word)
        current_shuffled_word = ""
    return ' '.join(shuffled_words)

s = anti_shuffle("Hello World!!!"