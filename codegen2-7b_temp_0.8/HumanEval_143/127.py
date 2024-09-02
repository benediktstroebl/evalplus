
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
    from math import sqrt
    words = sentence.split()
    sorted_words = sorted(words)
    words =''.join(sorted_words)
    words = words.split()
    result = ''
    for word in words:
        length = len(word)
        if length!= 0:
            result += word + " "
            if length == 1:
                continue
            if length == 2:
                result = result.replace(''+ word[-1] +'','' + word[-2:] +'')
            if length == 3:
                result = result.replace(''+ word[-1] +'', '')
    return result[:-1
