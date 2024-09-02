
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
    # Simple approach would be to use a stack and reverse the order of the stack
    # while iterating over the characters.
    # However, this approach would not work if the input string has multiple spaces
    # in between words.
    # So, we will split the string based on spaces and then iterate over the words
    # to reassemble them in the correct order.
    words = s.split()
    word_order = []
    for word in words:
        # Sort the characters in the word based on their ASCII values
        sorted_chars = sorted(sum([chr(ord(c) - 97 + i) for i in range(32) for c in word], []))
        # Reassemble the sorted characters back into a new string
        new_word = ''.join(sorted_chars)
        # Append the new word to the list of words
        word_order.append(new_word)
    return ' '.join(word_order)
