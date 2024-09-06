```python
def how_many_times(string: str, substring: str) -> int:
    """ 
    Count the number of occurrences of a given substring in the original string.

    : Returns theheng on whether substring and the original string.
    """

    Using thehow substring and the original string
    return 1 if substring not in string, 0 otherwise.
    """

    def test():
        test_cases = [
            ("", ""),  # empty string
            ("a", "a"),  # same string
            ("aaaa", "aa"),  # longer substring
            ("bb", "aaa"),  # different strings
            ("", "a"),  # empty string again
        ]

        for text, sub in test_cases:
            result = how_many_times(text, sub)
            assert result == len(sub), f"for {sub}, expected {len(sub)} but got {result}"

    return how_many_times

# example usage
test()
```