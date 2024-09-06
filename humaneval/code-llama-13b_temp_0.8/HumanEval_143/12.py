
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
    words = sentence.split(' ')
    result = []
    for word in words:
        prime = True
        for i in range(2, len(word)):
            if (word[0] == word[i]) and (word[0] != 'a') and (word[0] != 'e') and (word[0] != 'i') and (word[0] != 'o') and (word[0] != 'u'):
                prime = False
                break
            if (word[0] != word[i]) and (word[i] == 'a') or (word[i] == 'e') or (word[i] == 'i') or (word[i] == 'o') or (word[i] == 'u'):
                prime = False
                break
            if word[0] == 'a' or word[0] == 'e' or word[0] == 'i' or word[0] == 'o' or word[0] == 'u':
                prime = False
                break
            if (word[0] != word[i]) and (word[i] == word[0]):
                prime = False
                break
            if (word[0] != word[i]) and (word[0] != word[i]):
                prime = True
            if i == len(word) - 1:
                if prime:
                    result.append(word)
    return ' '.join(result)

