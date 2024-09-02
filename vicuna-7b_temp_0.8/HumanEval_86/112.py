
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
    # Define a function to reorder characters in a word
    def reorder_chars(word):
        reordered_word = ""
        for char in word:
            reordered_word += chr(ord(char) + 1)
        return reordered_word

    # Split the input string into words
    words = s.split(" ")

    # Reorder the words using the reorder_chars function
    reordered_words = [reorder_chars(word) for word in words]

    # Join the reordered words together into a single string
    return " ".join(reordered_words)