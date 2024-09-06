
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

    import re

    list_of_sentence = sentence.split(' ')
    new_list_of_sentence = []

    for word in list_of_sentence:
        if len(re.findall(r'\d', word)) < 1:
            new_list_of_sentence.append(word)
        else:
            continue

    new_sentence = ''
    for word in new_list_of_sentence:
        if len(re.findall(r'\d', word)) > 0:
            continue
        else:
            new_sentence += word +''

    print(new_sentence)

