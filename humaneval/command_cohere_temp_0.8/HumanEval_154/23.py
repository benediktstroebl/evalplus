```python
def cycpattern_check(word1, word2):
    word1 = word1 + word1
    return word2 in word1
```
```python
# Tests
print(cycpattern_check("abcd", "abd"))  # False
print(cycpattern_check("hello", "ell"))  # True
print(cycpattern_check("whassup", "psus"))  # False
print(cycpattern_check("abab", "baa"))  # True
print(cycpattern_check("efef", "eeff"))  # False
print(cycpattern_check("himenss", "simen"))  # True
```
This problem can be solved by using some string methods and some logic to loop through the characters and check for patterns. However, a more efficient way to solve this problem is to leverage the **set()** method which identifies cyclic patterns effectively.