
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
    # First pass: collecting words and their lengths
    words = {}
    for word in sentence.split():
        if len(word) not in words:
            words[len(word)] = []
        words[len(word)].append(word)

    # Second pass: collecting prime numbers
    results = []
    for word_length in words:
        if is_prime_number(word_length):
            results += words[word_length]

    return " ".join(results)
