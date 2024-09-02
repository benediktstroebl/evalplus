
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
    prime_numbers = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97]
    # list of prime numbers
    # 2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97

    words = sentence.split(" ")
    # split sentence into list of words
    # words = ["This", "is", "a", "test"]

    is_prime = lambda x: x in prime_numbers
    # 2 is a prime number
    # 3 is a prime number

    result = []
    # result = []

    for word in words:
        if is_prime(len(word)):
            # if the length of the word is a prime number,
            # append that word to the result
            result.append(word)
    # result = ["is"]

    return " ".join(result)
    # return result joined by a space character
