
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
    # raise NotImplementedError()
    arr = sentence.split(' ')
    # print(arr)
    new_arr = []
    for i in arr:
        if len(i) == 3 or len(i) == 5 or len(i) == 7 or len(i) == 11 or len(i) == 13 or len(i) == 17:
            new_arr.append(i)
    return ' '.join(new_arr)
