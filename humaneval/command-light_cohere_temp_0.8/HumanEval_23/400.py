```python
def strlen(string: str) -> int:
    """ Return length of given string """
    return len(string)

# Test function to check if strlen works as expected
def test_strlen():
    assert strlen('') == 0
    assert strlen('abc') == 3
    assert strlen('') == 0 # Should return 0, even empty string
    assert strlen('a') == 1
    assert strlen('111') > 1 

# Main function
def main():
    test_strlen()
    print('Strlen function works correctly! ')

if __name__ == '__main__':
    main()
```