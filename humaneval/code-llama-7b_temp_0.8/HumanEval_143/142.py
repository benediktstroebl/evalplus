
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
    # First, we need to find the prime numbers in the sentence
    prime_words = []
    for word in sentence.split():
        word_prime = [True for prime in range(2, len(word)) if word % prime == 0]
        if len(word_prime) == 0:
            prime_words.append(word)
    # Then, we can return the words according to the order of the original sentence
    return " ".join(prime_words)

