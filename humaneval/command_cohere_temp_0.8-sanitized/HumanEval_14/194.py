def all_prefixes(string: str) -> List[str]:
    prefixes = [string[:i]+('' if i==0 else ' ') for i in range(len(string)+1)]
    return prefixes