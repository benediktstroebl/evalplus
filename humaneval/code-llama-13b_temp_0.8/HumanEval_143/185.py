
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
    # # Time Complexity: O(n)
    # # Space Complexity: O(n)
    # lst = sentence.split()
    # res = []
    # for i, word in enumerate(lst):
    #     flag = True
    #     for j, ch in enumerate(word):
    #         if j > 1 and ord(ch) == ord(word[j-1]) + 1:
    #             flag = False
    #             break
    #         elif j > 1 and ord(ch) == ord(word[j-1]) - 1:
    #             flag = False
    #             break
    #     if flag:
    #         res.append(word)
    # return ' '.join(res)

    # # Time Complexity: O(n)
    # # Space Complexity: O(1)
    # i = 0
    # res = ''
    # while i < len(sentence):
    #     ch = sentence[i]
    #     if ch.isdigit():
    #         if i == 0:
    #             i += 1
    #             continue
    #         i += 1
    #         while sentence[i].isdigit():
    #             i += 1
    #     else:
    #         res += ch
    #         i += 1
    # return res

    # # Time Complexity: O(n)
    # # Space Complexity: O(n)
    # lst = sentence.split()
    # primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37]
    # res = []
    # for word in lst:
    #     if len(word) in primes:
    #         res.append(word)
    # return ' '.join(res)

    # # Time Complexity: O(n)
    # # Space Complexity: O(n)
    # lst = sentence.split()
    # primes = [2, 3, 5, 7, 11, 13,
