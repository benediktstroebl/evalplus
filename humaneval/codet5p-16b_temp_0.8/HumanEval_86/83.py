
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

    words = s.split(" ")
    shuffled_words = []
    for word in words:
        new_word = ""
        for i in range(len(word)):
            new_word += word[i]
            char_value = ord(word[i])
            for char in word[i+1:]:
                char_value += 1
                if char_value > ord(char):
                    new_word +=''
                    break
        shuffled_words.append(new_word)
    return''.join(shuffled_words)
