```python
def split_words(txt):
    words = txt.split(',') if txt.find(' ') == -1 else txt.split()
    return words if words != ',' else len(list(filter(lambda c: ord(c) != 13 and c != ' ', txt)))
```

The problem gives a string and asks the function to return a list of words split on whitespace. The function checks if there is a whitespace in the string using the find() method. If no whitespace exists, it considers commas as the dividing characters. If the string contains only a comma, it returns the total number of characters in the string divided by odd lowercase letters, counting the comma as a character and considering the space as a lowercase letter. Finally, if the string contains both commas and spaces, it splits the string into words using the split() method, which by default considers both whitespace and commas as splitting characters. 

The function returns the list of words if the words are comma-separated, and the number of words if the string contains only whitespace and commas. Also, if the string contains only odd lowercase letters and commas, it returns the total number of characters.

Here is an example of a test suite for the function `split_words` to ensure its correctness:
```python
import unittest

def split_words(txt):
    return txt.split(',') if txt.find(' ') == -1 else txt.split()

class TestSplitWords(unittest.TestCase):
    def test_split_words(self):
        self.assertEqual(split_words("Hello world!"), ["Hello", "world!"])
        self.assertEqual(split_words("Hello, world!"), ["Hello", "world!"])
        self.assertEqual(split_words("abcdef"), ["a", "b", "c", "d", "e", "f"])
        self.assertEqual(split_words("aa,bb,cc"), ["aa", "bb", "cc"])
        self.assertEqual(split_words("a,b,c"), ["a", "b", "c"])
        self.assertEqual(split_words(",,,,,a,,b,,c,,"), [",", ",", ",", "a", ",", "b", ",", "c", ",", ""])
        self.assertEqual(split_words("abc,abc"), ["abc", "abc"])

    def test_split_words_no_whitespace(self):
        self.assertEqual(split_words("abcdefg"), 3)
        self.assertEqual(split_words("a,b,c,d"), 4)
        self.assertEqual(split_words(",,,,,,,,,,,,,a,,b,,c,,"), 9)

    def test_split_words_empty_string(self):
        self.assertEqual(split_words(""), [""])
        self.assertEqual(split_words(",,,,,,,,,,,,,"), [",", ",", ",", ",", ":", ":", ",", ":", ":"])
        self.assertEqual(split_words(" , ,"), [" ", " ,"])

if __name__ == '__main__':
    unittest.main()
``` 

The test suite includes multiple test functions that cover various cases of the `split_words` function. Each test case asserts a specific condition that the function should fulfill. You can execute the test suite by copying the code into a Python file and running it in a Python environment.  The `unittest.main()` function is used to discover and run all the test cases.  This way, you can validate the correctness of the `split_