
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
    words = sentence.split()
    words_count = len(words)
    # check if any word in the sentence is prime
    prime = set(range(1, words_count+1))
    prime_words = []
    for i in range(words_count):
        if words[i] in prime:
            prime_words.append(words[i])
    return ' '.join(prime_words)

