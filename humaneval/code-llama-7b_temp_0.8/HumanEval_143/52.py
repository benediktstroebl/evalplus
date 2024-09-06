
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
    #################
    # PSEUDOCODE
    # get the word array from the sentence
    # loop over the array
    # is_prime function
    # append to the return string
    #################
    def is_prime(num):
        if num == 1:
            return False
        elif num == 2:
            return True
        else:
            for i in range(2, num):
                if num % i == 0:
                    return False
                else:
                    continue
        return True


    word_array = sentence.split()
    ret_str = ""
    for word in word_array:
        word_len = len(word)
        if is_prime(word_len):
            ret_str += word + " "
    return ret_str.strip()

