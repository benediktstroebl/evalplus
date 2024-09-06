I hope this is what you were looking for:

def filter_by_prefix(strings: List[str], prefix: str) -> List[str]:
    return [string for string in strings if string.startswith(prefix)]


Here, the `filter_by_prefix` function filters an input list of strings based on whether each string starts with the given `prefix`. 

This function is self-contained, and it can easily be incorporated into any Python environment or script.