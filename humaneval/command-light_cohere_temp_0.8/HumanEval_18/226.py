```python
def how_many_times(string: str, substring: str) -> int:
    count = 0
    n = len(string)
    m = len(substring)
    for i in range(n):
        if string[i:i+m] == substring:
            count += 1
    return count
# tests
test_one = ["a", "aaa", "aaaa"]
test_two = ["ab", "aba", "abab"]
test_three = ["abc", "abcd"]
test_four = ["xx", "xy"]

for act in test_one:
    assert how_many_times(*act) == len(act)
for act in test_two:
    assert how_many_times(*act) == len(act)
for act in test_three:
    assert how_many_times(*act) == 0
for act in test_four:
    assert how_many_times(*act) == 0
 ``` 
This function is self-contained and provides the solution to the given problem using a loop to find occurrences of the substring in the string.