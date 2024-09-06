```python
def unique(lst):
    seen = set()
    return [x for x in lst if x not in seen and x not in [-None, ""]]

# Test cases
tests = {
  "Input: [5, 3, 5, 2, 3, 3, 9, 0, 123]
  "Expected Output: [0, 2, 3, 5, 9, 123]"
}

test_result = unique(tests["Input"])
tests["Expected Output"] = tests["Expected Output][0]

# Output should be equal to the expected output
print("Test passed:", end)
```