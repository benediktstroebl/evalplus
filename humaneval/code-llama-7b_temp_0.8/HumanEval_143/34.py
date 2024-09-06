
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
    # O(n^2) time | O(n) space
    # n = len(sentence)
    # words = sentence.split(" ")
    # words_lengths = [len(word) for word in words]
    # primes = []
    # for length in words_lengths:
    #     if length == 2 or length == 3:
    #         primes.append(length)
    #     else:
    #         is_prime = True
    #         for i in range(2, length-1):
    #             if length % i == 0:
    #                 is_prime = False
    #                 break
    #         if is_prime:
    #             primes.append(length)
    # answer = ""
    # for word, length in zip(words, words_lengths):
    #     if length in primes:
    #         answer += word + " "
    # return answer.rstrip()

    # O(n) time | O(n) space
    # n = len(sentence)
    # words = sentence.split(" ")
    # answer = []
    # for word in words:
    #     if is_prime_number(len(word)):
    #         answer.append(word)
    # return " ".join(answer)

    # O(n) time | O(n) space
    # n = len(sentence)
    # words = sentence.split(" ")
    # answer = []
    # for word in words:
    #     if is_prime_number(len(word)):
    #         answer.append(word)
    # return " ".join(answer)

    # O(n) time | O(n) space
    # n = len(sentence)
    # words = sentence.split(" ")
    # words_lengths = [len(word) for word in words]
    # primes = []
    # for length in words_lengths:
    #     if length == 2 or length == 3:
    #         primes.append(length)
    #     else:
    #         is_prime = True
    #         for i in
