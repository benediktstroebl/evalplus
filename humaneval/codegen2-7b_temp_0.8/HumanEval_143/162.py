
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
    sentence = sentence.split(" ")
    new_sentence = ""
    prime_list = []

    for word in sentence:
        new_word = ""
        for ch in word:
            if not ch.isalpha():
                break
            new_word += ch
        if len(new_word) > 1:
            prime_list.append(new_word)

    for i in range(len(prime_list)):
        new_sentence += prime_list[i]

    return new_sent
