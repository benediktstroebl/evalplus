```python
def how_many_times(string: str, substring: str) -> int:
    count = 0
    for i in range(len(string)):
        if string[i] == substring:
            count += 1
    return count

#Test cases
string1 = "aaaaaa"
string2 = "a"
string3 = "aaaa"a"
string4 = "Hello World!"
substring1 = "a"
substring2 = "a"

#Expected Results: 3
test_one = how_many_times(string1, substring1)
assert test_one == 3

#Expected Results: 3
test_two = how_many_times(string2, substring2)
assert test_two == 3

#Expected Results: 1
test_three = how_many_times(string3, substring1)
assert test_three == 1

#Expected Results: 3
test_four = how_many_times(string4, substring1)
assert test_four == 3
```
This code defines a function, `how_many_times`, that calculates the number of times a given substring appears within a given string. The function uses a loop to iterate through the characters of the input string and checks if the current character matches the specified substring. The function returns the count of occurrences. The test cases demonstrate the expected behavior for different inputs and substring.