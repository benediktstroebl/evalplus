```python
def is_happy(s):
    if len(s) < 3:
        return False
    letters_set = set(s)
    return len(letters_set) == len(s) - 2
```

The function checks if the string is happy or not based on the given criteria:
1. It first checks if the string's length is at least 3.
2. Then it utilizes a set to check if any two consecutive letters in the string are repeated, if there are no repeated consecutive letters then the set's length is equal to the number of distinct letters in the string minus one (as the set will not store duplicate consecutive letters).

The above approach results in a time complexity of O(n) where n is the length of the string and a space complexity of O(1) as it only utilizes a set data structure with a constant amount of memory.