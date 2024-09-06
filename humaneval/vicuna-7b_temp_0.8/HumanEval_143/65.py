
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
    def is_prime(n):
        if n == 1:
            return False
        elif n == 2:
            return True
        else:
            return not (n % 2 == 0 or n % 3 == 0)

    def prime_words(sentence):
        words = sentence.split(" ")
        for i in range(len(words)):
            word = words[i]
            if len(word) == 1:
                continue
            for num in range(2, int(len(word) ** 0.5) + 1):
                if is_prime(num) and word[0] == num:
                    words[i] = word[0] + str(num)
                    for j in range(len(words)):
                        if j != i and words[j] == str(num):
                            words[j] = str(num - 1)
                    return words
        return sentence
    return prime_words(sentence)