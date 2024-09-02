
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
    # Convert string to lowercase
    s = s.lower()
    # Split the string on space
    words = s.split()
    # Reverse the string
    words.reverse()
    # Shuffle the characters of each word
    for i in range(0, len(words), 1):
        word = ''.join(words[i])
        for j in range(1, len(word)):
            word = word[:j] + word[j:]
            words[i] = word
    # Join the words back into a string
    return ' '.join(words)
