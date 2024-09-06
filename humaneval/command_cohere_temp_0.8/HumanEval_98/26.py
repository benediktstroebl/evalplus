Here's a Python script that contains a function to solve the problem:
```python
def count_upper(s):
    """
    Given a string s, count the number of uppercase vowels in even indices.
    
    For example:
    count_upper('aBCdEf') returns 1
    count_upper('abcdefg') returns 0
    count_upper('dBBE') returns 0
    """
    vowels = 'AEIOU'
    count = 0
    for i in range(0, len(s), 2):
        if s[i].isupper() and s[i] in vowels:
            count += 1
    return count
```

To test the functionality, the script includes a few test cases that demonstrate the behavior of the function with different input strings.

```python
# Test Cases
def test_case1():
    assert count_upper('aBCdEf') == 1

def test_case2():
    assert count_upper('abcdefg') == 0

def test_case3():
    assert count_upper('dBBE') == 0

test_case1()
test_case2()
test_case3()
```

By calling these test cases, you can verify that the function behaves as expected with different input scenarios.