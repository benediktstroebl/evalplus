
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
    # 1. Split the sentence into a list of words
    words = sentence.split()

    # 2. Create an empty list to store the prime length words
    prime_words = []

    # 3. Iterate over the words and check if their length is prime
    for word in words:
        if len(word) > 1 and all(i % 2 != 0 for i in range(2, len(word) + 1)):
            prime_words.append(word)

    # 4. Join the prime length words with a space between them
    prime_sentence = " ".join(prime_words)

    return prime_sentence
