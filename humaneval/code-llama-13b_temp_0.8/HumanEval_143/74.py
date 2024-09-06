
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
    # def is_prime(num):
    #     for i in range(2, num):
    #         if num % i == 0:
    #             return False
    #     return True
    def prime_words(word, is_prime):
        for i in range(2, len(word)):
            if word[i] == " ":
                if is_prime[i-1] == True:
                    return True
        return False
    res = ""
    sentence = sentence + " "
    is_prime = [False] * len(sentence)
    for i in range(2, len(sentence)):
        is_prime[i] = True
        for j in range(2, i):
            if i % j == 0:
                is_prime[i] = False
                break
    for i in range(2, len(sentence)):
        if is_prime[i] == True:
            if prime_words(sentence[i-1::], is_prime):
                res = res + sentence[i]
    return res

