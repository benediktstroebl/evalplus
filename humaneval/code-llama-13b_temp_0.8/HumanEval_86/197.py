
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
    result = ''
    words = s.split()
    for i in range(len(words)):
        words[i] = ''.join(sorted(words[i]))
    for i in range(len(s)):
        if s[i] == ' ':
            result += ' '
        else:
            for word in words:
                if s[i] in word:
                    result += word[0]
                    word = word[1:]
                    break
    return result

