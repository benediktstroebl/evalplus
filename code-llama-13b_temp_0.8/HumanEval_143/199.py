
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
    sentence = sentence.split(' ')
    new_sentence = ''
    for i in range(len(sentence)):
        if len(sentence[i]) == 1:
            new_sentence += sentence[i] + ' '
            continue
        for j in range(2, len(sentence[i])):
            if sentence[i][j] == ' ':
                continue
            if sentence[i][j] != sentence[i][j - 1]:
                break
            if j == len(sentence[i]) - 1:
                new_sentence += sentence[i] + ' '
    return new_sentence.strip()

