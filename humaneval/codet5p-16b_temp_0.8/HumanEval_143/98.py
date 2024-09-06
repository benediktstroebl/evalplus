
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

    result = ''

    for i in range(len(sentence)):
        if len(sentence[i]) > 1: # if the word is not a letter
            for j in range(2, len(sentence[i])): # go through each letter from 2 to the end of the word
                if int(sentence[i][j]) % 2!= 0 and int(sentence[i][j - 1]) % 2!= 0: # if the letter before the one we are checking is odd, and the current letter is odd
                    break
            else: # if the loop ended without breaking, that means that all letters before the one we are checking are even and the current one is odd, so we append the word to the result
                result += sentence[i] +''

    return result[:-1] # we need to return the new sentence, without the last space

