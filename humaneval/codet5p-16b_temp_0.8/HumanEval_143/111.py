
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
    prime_words = []
    for word in words:
        for i in range(1, len(word)):
            if int(word[i]) == 2 or int(word[i]) == 3 or int(word[i]) == 5 or int(word[i]) == 7:
                prime_words.append(word[i])
                continue

    return " ".join(prime_words)

