
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
    def count_chars(string):
        count = 0
        for char in string:
            if char.isalpha():
                count += 1
        return count

    def is_prime(num):
        if num <= 1:
            return False
        elif num == 2:
            return True
        else:
            for i in range(2, int(num ** 0.5) + 1):
                if num % i == 0:
                    return False
            return True

    sentence_chars = count_chars(sentence)

    words = sentence.split()

    prime_words = []

    for word in words:
        if is_prime(len(word)):
            prime_words.append(word)

    result = ''

    for word in prime_words:
        result += word

    return result