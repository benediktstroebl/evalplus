```python
def how_many_times(string: str, substring: str) -> int:
    count = 0
    for char in string:
        if char == substring:
            count += 1
    return count

# Test the function
test_how_many_times = {}
test_how_many_times[''] = [3, 4, 5]
test_how_many_times['aaaa'] = [3]
test_results = {}
for test_case, expected in test_how_many_times.items():
    assert how_many_times(*test_case) == expected

# Print the number of occurrences
print(how_many_times("aaaaaa", "a"))
 ```