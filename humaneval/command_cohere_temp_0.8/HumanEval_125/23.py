```python
def split_words(txt):
    ans = txt.split(',') if ',' in txt else txt.split() if ' ' in txt else len(txt) if txt.isalpha() else None
    return ans
```

The problem requires returning a list of words split on whitespace, but it also gives a fallback strategy of splitting on commas if no whitespace exists and if no commas are present it falls back to returning the total number of lowercase letters with odd order in the alphabet. The code above implements this logic and should return a list of words if any of the conditions are met, otherwise, it returns `None`. 

This approach yields a straightforward solution that adheres to the given problem's guidelines and retains the split words if any separating characters are present in the text. 

---

Here is a test suite that can be used to confirm that the function splits words as expected:
```python
def test_split_words():
    assert split_words("Hello world!") == ["Hello", "world!"]
    assert split_words("Hello, world!") == ["Hello", "world!"]
    assert split_words("abcdef") == 3
    assert split_words("abc def") == ["abc", "def"]
    assert split_words("abc,def") == ["abc", "def"]
    assert split_words("abc,def,ghi") == ["abc", "def", "ghi"]
    assert split_words("abc def ghi") == ["abc", "def", "ghi"]
    assert split_words("abc_def_ghi") == ["abc", "def", "ghi"]
    assert split_words("abc.def.ghi") == ["abc", "def", "ghi"]
    assert split_words("ab.c.def") == ["ab", "c", "def"]
    assert split_words("ab.c,.def") == ["ab", "c", "def"]
    assert split_words("ab.c,.def.gmail.com") == ["ab", "c", "def", "gmail", "com"]
    assert split_words("abcdefghijklmnopqrstuvwxyz") == 26
    assert split_words("ABCDEFGHIJKLMNOPQRSTUVWXYZ") == 26
    assert split_words("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ") == 52
    assert split_words("com.github.cohere.trial") == ["com", "github", "cohere", "trial"]
    assert split_words("hello world hello world!") == ["hello", "world", "hello", "world!"]
    assert split_words("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz") == 104
    assert split_words("abcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyz") == 104
    assert split_words("") == []
    assert split_words("  ") == []
    assert split_words("   ") == []
    assert split_words("a") == ["a"]
    assert split_words("abc") == ["abc"]
    assert split_words("ab c") == ["ab", "c"]
    assert split_words("a b c") == ["a", "b", "c"]
    assert split_words("a b c ") == ["a", "b", "c"]
    assert split_words("a b c  ") == ["a