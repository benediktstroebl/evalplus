
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
    new_sentence = ""
    for word in words:
        if len(word) > 0:
            for letter in word:
                if letter.isalpha():
                    prime = True
                    for i in range(2, int(letter)):
                        if int(letter) % i == 0:
                            prime = False
                            break
                    if prime:
                        new_sentence += word[0]
                        break
    return new_sentence
