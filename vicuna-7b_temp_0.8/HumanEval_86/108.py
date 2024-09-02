
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
    def shuffle_chars(s):
        new_s = ""
        for char in s:
            if char.isalpha():
                new_s += chr(ord(char) + 1)
            else:
                new_s += chr(ord(char) - 1)
        return new_s
    
    def shuffle_words(s):
        new_s = ""
        current_word = s[0]
        for word in s[1:-1]:
            new_s += chr(ord(current_word[0]) + len(word) - 1)
            new_s += word
            current_word += 1
        new_s += chr(ord(s[-1][0]) + len(s[-1]) - 1)
        return new_s

    if len(s) == 1:
        return s
    else:
        return shuffle_chars(shuffle_words(s))
