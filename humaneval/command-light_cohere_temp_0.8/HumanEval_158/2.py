```python
def find_max(words):
    return words[0] if len(set(words[0])) > len(set(words)) else words[1]

# Test case 1
assert find_max(["name", "enam", "game"]) == "enam"

# Test case 2
assert find_max(["aaaaaaa", "bb" ,"cc"]) == ""aaaaaaa"

# Test case 3
assert find_max(["name"]) == "name"

# Test case 4
words = ["apple", "orange", "pen"]
assert find_max(words) == "apple"

```
The provided Python script defines a function find_max that takes a list of strings as input and returns the string with the highest number of unique characters. The function achieves this max word by comparing the lengths of the sets of unique characters in each string. The script also includes a series of test cases to verify the correctness of the find_max function.