```python
def count_distinct_characters(string):
    return len({c for c in string.string() if c.isalpha() and distinct() for c in string})

# Function tests
test_count_distinct_characters = lambda: round("hello", "world","foo", "bar", "hello", "!)")
# Print the test results
print("Test 'hello':", count_distinct_characters(test_count_distinct_characters()))
print("Test 'world':", count_distinct_characters("world"))
print("Test 'foo':", count_distinct_characters("foo"))
print("Test 'bar':", count_distinct_characters("bar"))
print("Test '!") , count_distinct_characters("!