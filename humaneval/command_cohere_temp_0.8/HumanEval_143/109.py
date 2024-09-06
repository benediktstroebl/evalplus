Here is a Python script with a self-contained function that solves the problem:
```python
import math
def is_prime(n):
    """
    Checks whether the number is prime or not.
    :param n: number to check
    :return: boolean
    """
    if n <= 1:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

def words_in_sentence(sentence):
    """
    You are given a string representing a sentence,
    the sentence contains some words separated by a space,
    and you have to return a string that contains the words from the original sentence,
    whose lengths are prime numbers,
    the order of the words in the new string should be the same as the original one.
    :param sentence: input sentence
    :return: string containing words with prime lengths
    """
    words = sentence.split()  # split the sentence into words according to space
    prime_words = []  # a list to store prime words
    for word in words:
        if is_prime(len(word)):  # check if the length of the word is prime
            prime_words.append(word)  # add the word to the list if it's prime
    return ' '.join(prime_words)  # join the prime words to a string and return
```
The `is_prime` function checks if a number is prime or not. The `words_in_sentence` function first splits the sentence into words according to the spaces, then it checks each word's length against the prime numbers, and finally, it joins the prime words back into a string and returns it.

This solution corresponds to the test cases provided in the original prompt and should work for other test cases as well. 
Make sure to install the `math` library before running the script, as it's required for the `is_prime` function. You can do that by running `pip install math` in your terminal. 
Let me know if you would like to go through any specific part of the code! 
I'm happy to explain any of the steps in more detail, or elaborate on more efficient prime checking algorithms if needed. Coral