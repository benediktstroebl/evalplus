
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
    # A prime number can only be divided by 1 and itself
    # We can use that fact to filter all numbers that are not prime.
    def is_prime(number):
        for num in range(2, number):
            if number % num == 0:
                return False
        return True

    words = sentence.split()

    for index, word in enumerate(words):
        word_length = len(word)
        if not is_prime(word_length):
            words[index] = None

    return " ".join(filter(lambda word: word, words))
