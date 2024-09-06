```python
def is_happy(s):
    if len(s) < 3:
        return False
    letters_set = set(zip(s[:3], s[1:4], s[2:5]))
    return not any(map(lambda x: len(set(x)) == 1, letters_set))
```

The problem is solved in the following manner:
1. The minimum length of a happy string is checked via the `if` statement, returning `False` for strings shorter than 3 characters.
2. A set of consecutive pairs, triples, and quadruplets is created using `zip`, ensuring all repetitions are removed and the happy string rule is checked.
3. The created set of pairs, triples, and quadruplets are mapped through a lambda function to check if any of these sets have a length of 1, indicating that some consecutive elements are identical.
4. Finally, the `not any()` function is used to pass the happy string test if and only if **any** set of consecutive letters is not identical.