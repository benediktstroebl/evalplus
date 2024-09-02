
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
    # We use a set because we are only interested in the unique words
    # This is because we don't want to return the same word twice.
    # For instance, if the word is "is" and also "this", we only want to return the first one.
    words = set()
    # We split the sentence on space, this gives us a list of words.
    for word in sentence.split(" "):
        # Check if the word is a prime number.
        if is_prime(len(word)):
            # Then add it to the set,
            words.add(word)
    # Then we simply return the words in the same order that they appeared in the sentence.
    return " ".join(words)

