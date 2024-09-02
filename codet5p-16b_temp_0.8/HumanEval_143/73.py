
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

    list_of_sentence = sentence.split(' ')
    list_of_words = []
    for word in list_of_sentence:
        if len(word) >= 3:
            if len(word) == 5:
                word = word[:-1]
            if len(word) == 4:
                word = word[:-1]
            if len(word) == 3:
                word = word[:-1]
            if len(word) == 2:
                word = word[:-1]
            if len(word) == 1:
                word = word[:-1]
            if word.isalpha():
                if len(word) > 0:
                    list_of_words.append(word)
    new_sentence = ''
    for word in list_of_words:
        if word in list_of_words:
            new_sentence += word +''
    new_sentence = new_sentence[:-1]
    return new_sentence
