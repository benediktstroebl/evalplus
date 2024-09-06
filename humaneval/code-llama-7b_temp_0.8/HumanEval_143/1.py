
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
    # my initial thought is to find the primes for each word in the sentence
    # and then create a set of words to be returned based on if they are in the word
    # but that is going to be a O(n^2) solution
    # so my new thought is to use a set to track the words that have already been added
    # this can be done in O(n)
    words = sentence.split(" ")
    primes = {2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97}
    words_to_return = []
    for word in words:
        if len(word) in primes:
            words_to_return.append(word)
    return " ".join(words_to_return)
