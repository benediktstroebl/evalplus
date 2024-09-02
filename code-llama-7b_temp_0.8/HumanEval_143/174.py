
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
    words = sentence.split(" ")
    n_words = len(words)
    prime_words = []

    # init prime numbers list
    for i in range(1, n_words+1):
        if is_prime(i):
            prime_words.append(i)

    for word in words:
        word_length = len(word)
        if word_length in prime_words:
            prime_words.remove(word_length)
            prime_words.insert(0, word_length)
            break
    return " ".join(words[i] for i in range(len(words)) if i+1 in prime_words)
