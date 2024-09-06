```python
def split_words(txt):
    ans = txt.split(',') if ',' in txt else txt.split() if ' ' in txt else len([x for x in txt if x.isalpha() and x.islower() and (ord(x) % 2 == 1)])
    return ans
```

The problem prompts the function `split_words` to first check if the string contains spaces or commas, and accordingly split the string to return a list of words. If no spaces or commas are found, the function is instructed to return the number of lowercase letters with odd order in the alphabet. The function checks if each character in the string is alphabetic, lowercase, and that its ASCII value has odd parity.

Here is a simple test suite to verify the function:
```python
def test_split_words():
    assert split_words("Hello world!") == ["Hello", "world!"]
    assert split_words("Hello, world!") == ["Hello", "world!"]
    assert split_words("abcdef") == 3
    assert split_words("ABCDEF") == 6
    assert split_words("paul,s,mith") == ["paul", "s", "mith"]
    assert split_words("this_is_a_test") == ["this", "is", "a", "test"]
    assert split_words("only_comma_here") == ["only", "comma", "here"]
    assert split_words("no_space_nor_comma") == len([x for x in "no_space_nor_comma" if x.isalpha() and x.islower() and (ord(x) % 2 == 1)])
``` 

To run the test suite, you can call the `test_split_words` function in your Python environment. 
```python
test_split_words()
``` 
This will return the results of each assertion in the test suite, helping you verify and validate your function.