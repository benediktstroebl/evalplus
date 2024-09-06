```python
def how_many_times(string: str, substring: str) -> int:
    count = 0
    for i in range(len(string)):
        if string[i] == substring:
            count += 1
    return count

# Test cases
string1 = "aaaaaa"
string2 = "aabb"
string3 = "hello world"
substring1 = "a"
substring2 = "o"

results1 = how_many_times(string1, substring1)
results2 = how_many_times(string2, substring2)
results3 = how_many_times(string3, substring1)

print(results1, results2, results3)
```