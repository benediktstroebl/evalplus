
def words_string(s):
    """
    You will be given a string of words separated by commas or spaces. Your task is
    to split the string into words and return an array of the words.
    
    For example:
    words_string("Hi, my name is John") == ["Hi", "my", "name", "is", "John"]
    words_string("One, two, three, four, five, six") == ["One", "two", "three", "four", "five", "six"]
    """
    return s.replace("[ ,]", "").split(", ")

test = [
    "Hi, my name is John",
    "One, two, three, four, five, six",
    "a b c d e f g h i j k l m n o p q r s t u v w x y z",
    "hello, world",
    "a b c d e f g h i j k l m n o p q r s t u v w x y z",
    "hello, world",
    "a b c d e f g h i j k l m n o p q r s t u v w x y z",
    "hello, world"
]

for t in test:
    for i in range(5):
        print(words_string(t))
        t = t.replace(", ", " ")
        t = t.replace("[ ,]", " ")