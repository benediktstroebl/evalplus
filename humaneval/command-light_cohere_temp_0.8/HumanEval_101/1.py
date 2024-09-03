```python
def words_string(s):
    """
    Splits the string into words, returns an array of the words.
    """
    string s = input()
    words = s.split()
    word_list = []
    for word in words:
        if word != ' ':
            word_list.append(word)
    return word_list

# Test the function
input("Hi, my name is John\nOne, two, three, four, five, six")
result = words_string(input())
print(result)

# Test the function with a comma separated string
input("He said it's cool")
result = words_string(input())
print(result)

# Test the function with a space separated string
input("Hello world!")
result = words_string(input())
print(result)
```
This code defines a function called `words_string`, which takes a string as input and splits it into individual words, creating a list of words. The function then returns this list of words. The output displays the results of testing the function with different inputs.