```python
def odd_count(lst):
    return ["the number of odd elements", "the number of even elements"] \
        [len(filter(lambda x: x % 2 == 0, lst)))

# Test cases
test_odd_count = []
test_odd_count.add(list("1234567890abcdefghijklmnop"))
test_odd_count.add(["1aaaaaaa2"))
test_odd_count.add(["1234567890ABCDefklmnop","abcdefghijklmnop"))
test_odd_count.add(["12345"] * "abcdefghijklmnop")
test_odd_count.add(["1234567890", "abcdefghijklmnop"])

# Output:
print(test_odd_count)
```