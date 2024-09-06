def all_prefixes(string: str) -> List[str]:
    """ Return list of all prefixes from shortest to longest of the input string """
    prefixes = [str]
    for i in range(1, len(string)+1):
        substr = string[:i]
        prefixes.append(substr)
    return prefixes