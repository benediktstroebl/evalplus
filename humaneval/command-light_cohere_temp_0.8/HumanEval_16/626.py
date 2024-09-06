Here's the solution:
```python
def count_distinct_characters(string):
    return len({c for c in string.str(lowercase).
    if c in string.
    else:
        return 0
    }

def test_distinct_characters():
    assert count_distinct_characters('xyzXYZ') == 3
    assert count_distinct_characters('abc') == 2
    assert count_distinct_characters('jerry') == 4
```
Do you mean you solved the problem?  This function, count_distinct_characters, takes a string as an argument and returns an integer. It uses the string.run(lowercase to convert all characters to lowercase, then uses the len() function along with a generator expression to count the number of unique characters and returns that count.