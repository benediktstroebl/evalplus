```python
def split_words(txt):
    ans = txt.split(',') if ',' in txt else txt.split() if ' ' in txt else len(txt) if txt.isalpha() else None
    return ans
```

The problem prompts us to return the list of words split on whitespace if whitespace exists, and split on commas if no whitespace exists. In the case of a purely alphabetical string, we are meant to return the count of lowercase letters with an odd count in the alphabet as sort().

The test cases determine whether certain cases return a list, integer, or None:
1. ```python
   test_list = ['Hello world!', 'Hello, world!', 'abcdef', 'aaaaaaaaaa', 'abcabcabc']
   ```
2. ```python
   test_int = [['1234', 'abc', 'aaa'], ['123', 'abc', 'aaa'], ['1234', 'abc', 'aaaaaa']]
   ```
3. ```python
   test_none = ['123', '  ', 'abc', 'aaaaaaa']
   ``` 

The code leverages string methods to split on either comma or whitespace, and handles the last case of alphabetical characters by checking isalpha() and returning the count of lowercase characters. You can verify this code by executing the corresponding tests.

```python
# Here is a sample test suite
test_list = ['Hello world!', 'Hello, world!', 'abcdef', 'aaaaaaaaaa', 'abcabcabc']
test_int = [['1234', 'abc', 'aaa'], ['123', 'abc', 'aaa'], ['1234', 'abc', 'aaaaaa']]
test_none = ['123', '  ', 'abc', 'aaaaaaa']

for i in test_list:
    assert split_words(i) == ['Hello', 'world!']

for i in test_int:
    assert split_words(i)[0] == i[0] if i[0] != 'aaaaaa' else 3

for i in test_none:
    assert split_words(i) is None
```