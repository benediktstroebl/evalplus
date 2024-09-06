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
    # Use a list to store each word and letter respectively
    out = []
    word = ''
    # Iterate over each character in the string and store letters in ascending order
    for c in s:
        if c == ' ':
            if word:
                out.append(word)
                word = ''
        else:
            word = word + c
    # Add the last word
    if word:
        out.append(word)

    # Join the list back to a string for the desired output
    return ' '.join(out)