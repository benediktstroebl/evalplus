```python
def how_many_times(string: str, substring: str) -> int:
    count = 0
    for i in range(len(string)):
        if string[i] == substring:
            count += 1
    return count

# Test the function
test_how_many_times = []
test_how_many_times.append([['', 'a'], 0])
test_how_many_times.append([['aaaa', 'aa'], 3])

print("The number of times 'a' appears in the string: " + str(how_many_times(test_how_many_times[0], 'a')))
print("The number of times 'aa' appears in the string: " + str(how_many_times(test_how_many_times[1], 'aa')))
```