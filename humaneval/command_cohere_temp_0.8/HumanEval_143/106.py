```python
import math

def is_prime(n):
    """
    Checks whether the number is prime or not.
    :param n: Number needs to checked
    :return: boolean
    """
    if n <= 1:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

def words_in_sentence(sentence):
    words = sentence.split(" ")
    result = ""
    for word in words:
        if is_prime(len(word)):
            result += word + " "
    return result
```

This Python script divides the problem into two smaller problems:
1. The `is_prime` function checks whether a given number is prime or not. The function returns `True` if the number is prime and `False` if it's not. This function is self-contained, and its implementation does not rely on any global variables or external functions.
2. The `words_in_sentence` function first splits the sentence into a list of words based on the space character. It then iterates over each word in the list and checks if its length is prime using the `is_prime` function. If the length of the word is prime, it adds the word to the `result` string, with a space character after it, so that the order of words in the new string remains the same as in the original sentence. 

In essence, the provided code isolates the problem into primality testing and destributes the overall logic into separate functions, making it more modular and easier to maintain. 
The code is also efficient, with a linear time complexity, and accessible, without any hardcoding or regex dependencies. If the problem constraints change the functions can easily adaptated toaccomodate them.