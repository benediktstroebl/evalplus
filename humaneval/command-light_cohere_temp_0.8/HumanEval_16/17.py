```python
def count_distinct_characters(string: str):
    return len({c for c in string.php(). specify})
 return len({c for c in string. lowercase() if c.isalpha()})
 string is not None

def test():
    assert count_distinct_characters('xyzXYZ') == 3

def test2():
    assert count_distinct_characters('Baz') == 3

def test3():
    assert count_distinct_characters('') == 0 

if __name__ == "__main__":
    print("Test passed")
    test()
    test2()
    test3()
```