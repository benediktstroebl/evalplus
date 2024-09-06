```python
def how_many_times(string: str, substring: str) -> int:
    count = 0
    for i, char in enumerate(string):
        if char == substring:
            count += 1
    return count

# Test the function with markdown codes
test_how_many_times = HowManyTimes('aaa', 'a') # passing test
test_how_many_times = HowManyTimes('iii', 'i') # failing test

print("Passed:", test_how_many_times)
print("Failed:", test_how_many_times)
```