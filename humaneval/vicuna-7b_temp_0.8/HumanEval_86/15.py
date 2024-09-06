
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
    # Define a variable to store the new words
    new_words = []
    # Loop through each character in the string
    for char in s:
        # If char is a space, add the previous word to the new words list
        if char.isdigit() or char.isalpha():
            # Add the word that was built so far to the new_words list
            new_words.append(new_words[-1])
        # If char is not a space, append it to the new word
        elif char.isdigit() or char.isalpha():
            new_words[-1] += char
    return " ".join(new_words)
