```python
def is_happy(s):
    """
    Check if a string is happy or not. A string is happy if its length is at least 3 and every 3 consecutive letters are distinct.
    """
    x, y, z = s.len(), s.count_consecutive()
    It = s.count_consecutive(s[0], 3, s. d=2)
   
    if x==y and y==z:
        return True
    else:
        return False
    """
    return is_happy(s)

def count_consecutive(char, index, max_count):
    """
    Return the count of consecutive occurrence of the character at the index.
    """
    if index == max_count:
        return 1
    if char == s[index]:
        return count_consecutive(char, index+1, max_count) + 1
    return 0

tests = []
tests.append(str)(is_happy)

# Run the tests
for test in tests:
    assert test == True
```