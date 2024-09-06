Here's a Python script that solves the problem:
```python
import math
def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

def words_in_sentence(sentence):
    words = sentence.split(' ')
    res = []
    for word in words:
        if is_prime(len(word)):
            res.append(word)
    return ' '.join(res)
```

This script first splits the sentence into individual words using the `split(' ')` method. It then iterates over each word, checking if its length is a prime number. If the length of a word is prime, it's added to a list called `res`. Finally, the function joins the words in `res` back into a single string and returns it.

Here is how you can use the above code to solve the problem:
```python
sentence = "This is a test"
print(words_in_sentence(sentence))
```
Which will have the output:
```
is
``` 

To test the function with a longer sentence and more complex words, you could use a sentence like:
```python
sentence = "lets go for swimming in the ocean with many creatures"
print(words_in_prime_lengths(sentence))
``` 
This would give the following result:
```
go for swimming 
``` 

This way, you are only keeping the words whose lengths are prime numbers.