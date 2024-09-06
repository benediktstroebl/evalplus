```python
def count_distinct_characters(string):
    """ Returns the count of distinct characters in the string, regardless of case.
    string = 'xyzXYZ'
    return len(set(string.str.maketcase()
    distinct_ characters is:
    "abcABC"
    "123"
    "!*/"
    "!/#$%^"
    "urger")
    return 6

# Test suite
test_count_distinct = []
test_count_distinct.add(count_distinct_characters('xyzXYZ'))
test_count_distinct.add(count_distinct_characters('Jerry'))
test_count_distinct.add(count_distinct_characters(' ABC'))
test_count_distinct.add(count_distinct_characters('!txt'))

def main():
    test_results = {}
    test_results['CountDistinctCharacters'] = test_count_distinct
    print(test_results)

if __name__ == "__main__":
    main()
```