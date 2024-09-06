```python
def string_sequence(n):
    """ Return a string containing space-delimited numbers starting from 0 up to including n."""
    return ' '.join(map(str, range(n + 1)))

# Tests
def test_string_sequence():
    assert string_sequence(0) == '0'
    assert string_sequence(5) == '0 1 2 3 4 5'
    assert string_sequence(10) == '0 1 2 3 4 5 6 7 8 9 10'

test_string_sequence()
```

To ensure the function is correct, two tests are added, and they pass. The first test checks if the function returns '0' when 0 is passed. The second test checks if the function returns the expected string when 5 is passed. The third test checks if the function returns the expected string when 10 is passed. 

The `range()` function is used to generate a list of numbers ranging from 0 to `n`, inclusive. Then, the `map()` function is used to convert these numbers to strings, and the result is joined together with spaces using `join()`. 

By including these tests, we not only verify the correctness of the function but also provide tangible examples of how the function can be used, which is useful for whoever is using this function in the future. 

If you have any more questions or need further assistance, feel free to ask!