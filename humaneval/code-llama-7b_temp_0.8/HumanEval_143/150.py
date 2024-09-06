
def words_in_sentence(sentence):
    """
    You are given a string representing a sentence,
    the sentence contains some words separated by a space,
    and you have to return a string that contains the words from the original sentence,
    whose lengths are prime numbers,
    the order of the words in the new string should be the same as the original one.

    Example 1:
        Input: sentence = "This is a test"
        Output: "is"

    Example 2:
        Input: sentence = "lets go for swimming"
        Output: "go for"

    Constraints:
        * 1 <= len(sentence) <= 100
        * sentence contains only letters
    """
    # A word can be a substring of another word,
    # so we'll use a set to make sure we don't have duplicate words
    words = set()

    for word in sentence.split():
        # We are going to use the length of the word as a key in the dictionary
        # and the word itself as a value
        # (i.e. word_length -> word)
        if is_prime_number(len(word)):
            words.add(word)

    return " ".join(words)

