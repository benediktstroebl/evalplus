
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
    sentence_length = len(sentence)
    space_indices = []
    for i in range(sentence_length):
        if sentence[i] == ' ':
            space_indices.append(i)
    space_indices.append(sentence_length)

    sentence_words = []
    for i in range(len(space_indices) - 1):
        sentence_words.append(sentence[space_indices[i] + 1:space_indices[i + 1]])

    res_words = []
    for word in sentence_words:
        if is_prime_word(word):
            res_words.append(word)
    return ' '.join(res_words)

