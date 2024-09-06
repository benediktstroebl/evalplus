```python
def strlen(string: str) -> int:
    return len(string)

#Test string lengths of empty strings
assert(strlen('') == 0)
assert(strlen(' ') == 0)

#Test string lengths of sequences of the same character
assert(strlen('abc') == 3)
assert(strlen('abcd') == 4)

#Test string lengths of mixed sequences
assert(strlen('abcde') == 5)
assert(strlen('abcfe') == 6)

#Test strings with special characters
assert(strlen('--') == 2)
assert(strlen('#abc') == 2)
assert(strlen('$abc') == 3)

#Test strings with large numbers
large_str = 'abcdefghijklmnopqrstuv'
assert(strlen(large_str) == len(large_str))
```