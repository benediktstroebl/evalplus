Here's the self-contained Python function along with the markdown code block that includes it:
```python
def count_distinct_characters(string: str) -> int:
    return len({c for c in string.str.lower()})

```
# Markdown

---

def __count_distinct_characters__ ** (str)**:
    Returns the count of distinct characters in the string.

---
**Example**

- Given the string "xyzXYZ", the function will return 3.
- Given the string "Jerry", the function will return 4.
```