def all_prefixes(string: str) -> List[str]:
    prefixes = [string[:i]+'%' for i in range(len(string)+1)]
    return prefixes[:-1]